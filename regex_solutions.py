# regex_solutions.py
# Only open this after trying regex_practice.py yourself.
# Keep this file in the same folder as regex_practice.py.

import regex_practice

SOLUTIONS = {
    1: r"^S",
    2: r"u$",
    3: r"^K.*[ai]$",
    4: r"hu",
    5: r"^.{4}$",
    6: r"(\w)\1",
    7: r"^b[ao]",
    8: r"^(?!S)",
    9: r"^.u",
    10: r"^.+um.+$",
    11: r"^[^T].*[ui]$",
    12: r"^(?=.{5})(?=.*o)",
}

regex_practice.run(SOLUTIONS)
