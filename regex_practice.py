# regex_practice.py
# HOW TO USE:
#   1. Find the ANSWERS dictionary near the bottom.
#   2. Type your regex between the quotes for each exercise.
#   3. Save, then run the file. It tells you PASS or FAIL.
#      On FAIL it shows which names you missed and which you matched by mistake.
# Do not look at regex_solutions.py until you have really tried!

import re

names = ["Mishu", "Nipu", "Shuvo", "Sumi", "Tumpa", "Roni", "Riya", "Adnan",
         "Ladoo", "Chumchum", "Kaju", "Pesta", "Modhu", "Babui", "Babu",
         "Tuktuki", "Piku", "Mumu", "Tutu", "Chotu", "Koko", "Nono", "Potol",
         "Boba", "Bhuto", "Khoka", "Khuki", "Dusto", "Shuo"]


def um_in_middle(n):
    return any(n[i:i + 2] == "um" and i > 0 and i + 2 < len(n)
               for i in range(len(n) - 1))


# (number, description, rule written in plain Python, flags, hint)
EXERCISES = [
    (1, "Names that START with S",
     lambda n: n.startswith("S"), 0, "use ^"),
    (2, "Names that END with u",
     lambda n: n.endswith("u"), 0, "use $"),
    (3, "Names that start with K AND end with a or i",
     lambda n: n[0] == "K" and n[-1] in "ai", 0, "^K ... then .* then [ai]$"),
    (4, "Names that contain 'hu' anywhere",
     lambda n: "hu" in n, 0, "just the letters"),
    (5, "Names with exactly 4 letters",
     lambda n: len(n) == 4, 0, "^ and $ and {4}"),
    (6, "Names with a doubled letter (like the oo in Ladoo)",
     lambda n: any(a == b for a, b in zip(n, n[1:])), 0,
     "a group and a backreference \\1"),
    (7, "Names starting with Ba or Bo (re.I is applied for you)",
     lambda n: n.lower().startswith(("ba", "bo")), re.I, "a class [ao]"),
    (8, "Names that do NOT start with S",
     lambda n: not n.startswith("S"), 0, "negative lookahead (?!S)"),
    (9, "Names whose SECOND letter is u",
     lambda n: n[1] == "u", 0, "^ then one any-character then u"),
    (10, "Names with 'um' strictly in the middle (a letter before and after)",
     um_in_middle, 0, "^.+ ... .+$"),
    (11, "Names ending in u or i, but NOT starting with T",
     lambda n: n.endswith(("u", "i")) and not n.startswith("T"), 0,
     "^[^T] then .* then [ui]$"),
    (12, "Names with 5 or more letters AND containing o",
     lambda n: len(n) >= 5 and "o" in n, 0,
     "two lookaheads at the start: (?=.{5}) and (?=.*o)"),
]


def run(answers):
    passed = 0
    for num, desc, rule, flags, hint in EXERCISES:
        pattern = answers.get(num, "")
        print(f"\nExercise {num}: {desc}")
        if not pattern:
            print(f"   (not attempted yet)   hint: {hint}")
            continue
        try:
            got = [n for n in names if re.search(pattern, n, flags)]
        except re.error as error:
            print("   Your pattern is not valid regex:", error)
            continue
        expected = [n for n in names if rule(n)]
        if got == expected:
            print("   PASS  ", got)
            passed += 1
        else:
            print("   FAIL")
            print("   you forgot to match:      ", [n for n in expected if n not in got])
            print("   you matched by mistake:   ", [n for n in got if n not in expected])
    print(f"\nScore: {passed} / {len(EXERCISES)}")


# ---------------------------------------------------------------
# WRITE YOUR ANSWERS HERE. Example: 1: r"^S",
# ---------------------------------------------------------------
ANSWERS = {
    1: r"",
    2: r"",
    3: r"",
    4: r"",
    5: r"",
    6: r"",
    7: r"",
    8: r"",
    9: r"",
    10: r"",
    11: r"",
    12: r"",
}

if __name__ == "__main__":
    run(ANSWERS)
