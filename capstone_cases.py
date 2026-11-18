"""Inputs named by the capstone criteria. The trial runner posts these strings."""

NOT_WRITING = [
    "!!! ??? ... ,,, ;;; --- ((( )))",
    "🙂🙃😀😃😄😁😆😅😂🤣" * 3,
    "#### $$$$ %%%% ^^^^ &&&& **** #### $$$$",
    "1234567890 1234567890 1234567890 1234567890",
    "---- ____ .... **** ~~~~ ++++ ==== ####",
]

WRITING = [
    "I stayed up until two finishing this draft. My sentences jump from three words to a whole line, and I keep changing the ending.",
    "The tap was dripping again. I put a bowl under it, missed, and spent the next ten minutes chasing water across the counter with a towel.",
    "We got to the platform as the doors were closing. Maya yelled for me to wait, then laughed because she had the tickets and I had the snacks.",
    "Chapter notes from Tuesday: the argument turns on one example, the harbor, and I still do not think the second paragraph earns that turn.",
    "Dear building manager, the hallway light on the third floor has been out since Monday. I carried groceries up in the dark and nearly missed a step.",
]

LATENCY_TEXT = (
    "I wrote this paragraph so a warm request would have something ordinary to score. "
    "It is about a walk to the store in the rain, a torn grocery bag, and the orange that "
    "rolled into the street. None of that is a calibration trick. It is just long enough "
    "that the model has a few sentences to read, and short enough that I can paste it "
    "into a log without filling the page."
)

# Not one of the five criteria. A single repeated letter still looks alphabetic
# to the ratio gate, which is the hole the gate does not close.
REPEATED_LETTER = "a" * 400
