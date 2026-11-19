"""
Signal one: the model signal.

This is the signal that "reads the text for meaning". It runs a language model
on your own machine and asks one question: **how predictable is this text?**

The idea is the one every AI-detection product is built on. A language model
writes by repeatedly picking a likely next word, so text a model produced tends
to be text a model finds easy to predict. Human writing wanders more — odd word
choices, abrupt turns, the specific rather than the typical.

The measure is called **perplexity**. Low perplexity means "I could have
guessed this"; high perplexity means "that surprised me". This module turns
that into a 0–1 score where **higher means more likely AI**.

    from detector import model_signal
    score = model_signal("some text")     # 0.0 human-ish … 1.0 AI-ish

Everything runs locally. No account, no key, no card.

⚠️ **The blind spot, which you have to name in Milestone 1.**

Predictability is not the same thing as authorship. What this signal actually
rewards is **common words in short, ordinary sentences** — and plenty of real
people write that way.

Someone writing in a second language, sticking to vocabulary they're sure of.
A younger writer. Anyone writing plainly on purpose. Measured against gpt2,
writing like that scores about as machine-like as machine writing does.

The reverse trips people up too: dense, ornate prose full of rare words often
scores as *human* on this signal, because rare words are exactly what a
language model fails to predict. Formality on its own doesn't decide it.

So the writers this signal is most likely to accuse are the ones with the
least room to argue back. That is structural rather than a bug you can fix,
and it is the person Milestone 1 asks you to follow through your service.

Don't take that on trust — it's a claim you can check. Milestone 4 has you run
four calibration inputs. Add a plainly-written human paragraph to them and see
for yourself where it lands.
"""

import functools
import math
import random
import signal
import threading
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError

import config

_model = None
_tokenizer = None
_model_lock = threading.Lock()
_executor = ThreadPoolExecutor(max_workers=2)


# Circuit breaker state for stretch goal: Second measured improvement
class CircuitBreaker:
    """
    Circuit breaker pattern to prevent cascading failures.
    
    States:
    - CLOSED: Normal operation, requests pass through
    - OPEN: Too many failures, requests fail fast
    - HALF_OPEN: Testing if service recovered
    """
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"
    
    def __init__(self, failure_threshold: int = 3, reset_timeout: float = 30.0):
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.last_failure_time: float | None = None
        self.state = self.CLOSED
        self._lock = threading.Lock()
    
    def record_success(self) -> None:
        with self._lock:
            self.failure_count = 0
            self.state = self.CLOSED
    
    def record_failure(self) -> None:
        with self._lock:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.failure_threshold:
                self.state = self.OPEN
    
    def can_proceed(self) -> bool:
        with self._lock:
            if self.state == self.CLOSED:
                return True
            if self.state == self.OPEN:
                if self.last_failure_time and (time.time() - self.last_failure_time) > self.reset_timeout:
                    self.state = self.HALF_OPEN
                    return True
                return False
            # HALF_OPEN: allow one request to test
            return True
    
    def get_state(self) -> str:
        return self.state


_circuit_breaker = CircuitBreaker(failure_threshold=3, reset_timeout=30.0)


class DetectorUnavailable(RuntimeError):
    """The model couldn't be loaded — no download yet, or no disk."""


class DetectorTimeout(RuntimeError):
    """The model inference timed out."""


class TransientError(RuntimeError):
    """A transient error that may succeed on retry."""


def retry_with_backoff(max_attempts: int | None = None, base_delay: float | None = None):
    """Decorator for retry with exponential backoff on transient failures."""
    if max_attempts is None:
        max_attempts = config.RETRY_MAX_ATTEMPTS
    if base_delay is None:
        base_delay = config.RETRY_BASE_DELAY_SECONDS

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except TransientError as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        delay = min(
                            base_delay * (2 ** attempt) + random.uniform(0, 0.1),
                            config.RETRY_MAX_DELAY_SECONDS
                        )
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


def _load():
    """Load the model once and keep it. First call downloads ~550 MB."""
    global _model, _tokenizer
    with _model_lock:
        if _model is not None:
            return _model, _tokenizer

        try:
            import torch  # noqa: F401
            from transformers import AutoModelForCausalLM, AutoTokenizer
        except ImportError as exc:
            raise DetectorUnavailable(
                f"transformers or torch isn't installed ({exc}).\n"
                f"Run: pip install -r requirements.txt"
            ) from exc

        try:
            _tokenizer = AutoTokenizer.from_pretrained(config.DETECTOR_MODEL)
            _model = AutoModelForCausalLM.from_pretrained(config.DETECTOR_MODEL)
            _model.eval()
        except Exception as exc:  # noqa: BLE001
            raise DetectorUnavailable(
                f"Couldn't load '{config.DETECTOR_MODEL}': {exc}\n"
                f"The first run downloads about 550 MB — check your connection and "
                f"that you have disk space free."
            ) from exc

        return _model, _tokenizer


def _perplexity_inner(text: str) -> float:
    """
    Inner perplexity computation without timeout handling.
    """
    import torch

    model, tokenizer = _load()

    encoded = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=config.DETECTOR_MAX_TOKENS,
    )
    input_ids = encoded["input_ids"]

    if input_ids.shape[1] < 3:
        raise ValueError("Text is too short to score — a few sentences at least.")

    with torch.no_grad():
        output = model(input_ids, labels=input_ids)

    return float(math.exp(output.loss.item()))


def perplexity(text: str, timeout: float | None = None) -> float:
    """
    How surprised the model is by this text. Lower means more predictable.

    Returns a positive number. Typical values land roughly between 10 and 200,
    but that range shifts with topic and length, which is one reason the raw
    number isn't what you score on.

    If timeout is provided and exceeded, raises DetectorTimeout.
    """
    if timeout is None:
        timeout = config.MODEL_TIMEOUT_SECONDS

    future = _executor.submit(_perplexity_inner, text)
    try:
        return future.result(timeout=timeout)
    except FuturesTimeoutError:
        future.cancel()
        raise DetectorTimeout(f"Model inference timed out after {timeout}s")


@retry_with_backoff()
def model_signal(text: str, timeout: float | None = None) -> float:
    """
    The signal, as a 0–1 score. **Higher means more likely AI.**

    Perplexity is unbounded and roughly log-distributed, so it gets squashed
    onto 0–1 rather than clipped. The midpoint below is the perplexity that
    maps to 0.5 — text this surprising is a coin flip.

    You may want to move that midpoint once you've run the four calibration
    inputs in Milestone 4 and seen what your own text actually scores. If you
    do, say so in your README: it's a scoring decision, not a detail.

    Includes retry logic for transient failures and timeout handling.
    """
    ppl = perplexity(text, timeout=timeout)

    midpoint = 45.0    # perplexity that scores 0.5
    steepness = 1.6    # how sharply the score moves either side of it

    # Logistic on log-perplexity. Low perplexity -> high AI score.
    score = 1.0 / (1.0 + (ppl / midpoint) ** steepness)
    return round(min(max(score, 0.0), 1.0), 4)


def model_signal_with_fallback(text: str, timeout: float | None = None) -> tuple[float, bool]:
    """
    Model signal with graceful degradation and circuit breaker.

    Returns (score, degraded) where degraded=True means the model timed out,
    was unavailable, or the circuit breaker is open. Score defaults to 0.5 (neutral).
    """
    # Check circuit breaker first
    if not _circuit_breaker.can_proceed():
        return 0.5, True
    
    try:
        score = model_signal(text, timeout=timeout)
        _circuit_breaker.record_success()
        return score, False
    except (DetectorTimeout, DetectorUnavailable) as exc:
        _circuit_breaker.record_failure()
        return 0.5, True


def is_model_responsive(timeout: float = 2.0) -> bool:
    """
    Quick health check: can the model respond within timeout?
    Uses a short test string to verify model is loaded and responsive.
    """
    test_text = "This is a quick test to check if the model responds."
    try:
        _ = perplexity(test_text, timeout=timeout)
        return True
    except (DetectorTimeout, DetectorUnavailable, ValueError):
        return False


def get_circuit_breaker_state() -> dict:
    """Get current circuit breaker state for health checks."""
    return {
        "state": _circuit_breaker.get_state(),
        "failure_count": _circuit_breaker.failure_count,
        "can_proceed": _circuit_breaker.can_proceed(),
    }


def warm_up() -> str:
    """Load the model without scoring anything. Run this before class."""
    _load()
    return f"{config.DETECTOR_MODEL} loaded and ready."


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = (
            "The implementation of the proposed framework requires careful "
            "consideration of several key factors. First, it is important to "
            "note that the system must be able to handle a wide variety of "
            "different inputs. Additionally, the overall performance of the "
            "solution depends on a number of important variables."
        )
        print("(no text given — scoring a sample)\n")

    print(f"Loading {config.DETECTOR_MODEL} (first run downloads ~550 MB)…")
    print(f"perplexity     {perplexity(text):.1f}")
    print(f"model_signal   {model_signal(text):.4f}   (higher = more likely AI)")
