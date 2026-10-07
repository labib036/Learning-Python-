# regex_lessons.py
# Run this file and read the output next to the code.
# Change the patterns, run again, and watch what changes. That is how you learn.

import re

names = ["Mishu", "Nipu", "Shuvo", "Sumi", "Tumpa", "Roni", "Riya", "Adnan",
         "Ladoo", "Chumchum", "Kaju", "Pesta", "Modhu", "Babui", "Babu",
         "Tuktuki", "Piku", "Mumu", "Tutu", "Chotu", "Koko", "Nono", "Potol",
         "Boba", "Bhuto", "Khoka", "Khuki", "Dusto", "Shuo"]


def find(pattern, flags=0):
    """Return every name in the list that the pattern matches."""
    return [n for n in names if re.search(pattern, n, flags)]


def title(text):
    print()
    print("=" * 64)
    print(text)
    print("=" * 64)


def show(label, value):
    print(f"{label:<40} {value}")


# ---------------------------------------------------------------
title("LESSON 1: the main functions")
# ---------------------------------------------------------------
text = "Call 01711-223344 or 01811-556677 today"

show("search  (first match anywhere)", re.search(r"\d+", text).group())
show("match on digits (start only)", re.match(r"\d+", text))          # None
show("match on 'Call' (start only)", re.match(r"Call", text).group())
show("fullmatch (whole string)", re.fullmatch(r"\d+", "12345").group())
show("findall (all matches, a list)", re.findall(r"\d{5}-\d{6}", text))
show("sub (replace)", re.sub(r"\d", "#", text))
show("split (cut at matches)", re.split(r"\s+", text))

# ---------------------------------------------------------------
title("LESSON 2: anchors, any-character, and OR")
# ---------------------------------------------------------------
show("starts with S        ^S", find(r"^S"))
show("ends with a          a$", find(r"a$"))
show("exactly 4 letters    ^.{4}$", find(r"^.{4}$"))
show("contains hu          hu", find(r"hu"))
show("contains hu or o     hu|o", find(r"hu|o"))
show("Mi or Ni at start    ^(Mi|Ni)", find(r"^(Mi|Ni)"))
show("hu strictly inside   ^.+hu.+$", find(r"^.+hu.+$"))

# The famous mistake: spaces are real characters!
show("WRONG  'hu | o ' (has spaces)", find(r"hu | o "))               # []
show("RIGHT  'hu|o'", find(r"hu|o"))

# ---------------------------------------------------------------
title("LESSON 3: character classes")
# ---------------------------------------------------------------
show("starts with M or N   ^[MN]", find(r"^[MN]"))
show("starts with a vowel  ^[AEIOU]", find(r"^[AEIOU]"))
show("ends with a vowel    [aeiou]$", find(r"[aeiou]$"))
show("does not start w/ S  ^[^S]", find(r"^[^S]"))
show("digits    \\d", re.findall(r"\d", "a1b22"))
show("word chars \\w", re.findall(r"\w", "a_1 !"))
show("spaces    \\s", re.findall(r"\s", "a b\tc"))

# ---------------------------------------------------------------
title("LESSON 4: quantifiers (how many times)")
# ---------------------------------------------------------------
show("colou?r  (u optional)", re.findall(r"colou?r", "color colour"))
show("\\d{3}    exactly 3 digits", re.findall(r"\d{3}", "12 123 1234"))
show("\\d{3,}   3 or more", re.findall(r"\d{3,}", "12 123 1234"))
show("\\d{2,3}  2 to 3", re.findall(r"\d{2,3}", "1 12 123 1234"))
show("two u's   u.*u", find(r"u.*u"))
show("greedy  <.+>", re.search(r"<.+>", "<b>bold</b>").group())
show("lazy    <.+?>", re.search(r"<.+?>", "<b>bold</b>").group())

# ---------------------------------------------------------------
title("LESSON 5: groups")
# ---------------------------------------------------------------
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2026-10-07")
show("group(0) whole match", m.group(0))
show("group(1) year", m.group(1))
show("groups()", m.groups())

m = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})", "2026-10-07")
show("named groups", m.groupdict())

show("non-capturing (?:Mi|Ni)\\w+", re.findall(r"(?:Mi|Ni)\w+", "Mishu Nipu Roni"))
show("backreference (\\w)\\1 doubled", find(r"(\w)\1"))
show("findall with 2 groups", re.findall(r"([A-Z])(\d)", "A1 B2 C3"))

# ---------------------------------------------------------------
title("LESSON 6: flags")
# ---------------------------------------------------------------
show("^s  no flag", find(r"^s"))
show("^s  with re.I (ignore case)", find(r"^s", re.I))
multi = "ab\ncd\nef"
show("^\\w+ no flag", re.findall(r"^\w+", multi))
show("^\\w+ with re.M (each line)", re.findall(r"^\w+", multi, re.M))
show("a.b on 'a<newline>b' no flag", bool(re.search(r"a.b", "a\nb")))
show("a.b on 'a<newline>b' with re.S", bool(re.search(r"a.b", "a\nb", re.S)))

phone = re.compile(r"""
    (\d{5})    # first part
    -          # the dash
    (\d{6})    # second part
""", re.X)
show("verbose (re.X) pattern", phone.search("01711-223344").groups())

# ---------------------------------------------------------------
title("LESSON 7: lookaround (advanced)")
# ---------------------------------------------------------------
show("NOT starting with S  ^(?!S)", find(r"^(?!S)"))
show("number before ' taka'", re.findall(r"\d+(?= taka)", "50 taka, 20 dollars, 70 taka"))
show("number after $", re.findall(r"(?<=\$)\d+", "$30 and 40 and $50"))

strong = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
show("strong password 'Passw0rdX'", bool(re.search(strong, "Passw0rdX")))
show("strong password 'password'", bool(re.search(strong, "password")))

# ---------------------------------------------------------------
title("LESSON 8: replacing with sub")
# ---------------------------------------------------------------
show("swap date parts", re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", "2026-10-07"))
show("function as replacement", re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "a1 b22 c3"))
show("vowels become *", [re.sub(r"[aeiouAEIOU]", "*", n) for n in names[:5]])
show("count=2", re.sub("a", "X", "aaaa", count=2))
show("subn returns (text, count)", re.subn(r"\s+", " ", "a   b    c"))
show("clean extra spaces", re.sub(r"\s+", " ", "  too    many   spaces  ").strip())

# ---------------------------------------------------------------
title("LESSON 9: compile and finditer")
# ---------------------------------------------------------------
pat = re.compile(r"hu", re.I)
show("compiled pattern reused", [n for n in names if pat.search(n)])
for m in re.finditer(r"\d+", "a1 b22 c333"):
    print(f"   found {m.group():<4} at positions {m.span()}")

show("escape special characters", re.search(re.escape("a.b"), "xa.by").group())

# ---------------------------------------------------------------
title("LESSON 10: real-world patterns")
# ---------------------------------------------------------------
mail = "contact: fahim@example.com, sompa.k@mail.org"
show("emails", re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", mail))
show("dates", re.findall(r"\d{4}-\d{2}-\d{2}", "from 2026-10-07 to 2026-12-31"))
show("hex colors", re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}\b", "#fff and #1a2b3c"))

print("\nDone. Now open regex_practice.py")
