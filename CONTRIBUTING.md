# Contributing

Thanks for helping keep this current. Three kinds of contributions are most useful.

## Propose a new tell

Open a "New tell" issue first so the pattern can be discussed before code lands. A good proposal shows that the pattern appears across many generated sites (links or screenshots from several sources, not one), explains why it reads as unchosen, and suggests what to do instead.

Once agreed, a pull request should include all four of these:

1. A numbered entry in the right category in `vibecode-tells/SKILL.md`, with the tell, a one-line description, and an "Instead" alternative. New tells take the next number (31, 32, ...); numbers are never reused so old review reports stay readable.
2. A scanner rule in `vibecode-tells/scripts/scan.py`, if the tell is detectable from code. If it is not, add it to the manual-checks line instead.
3. A line in `tests/fixtures/vibecoded.html` that triggers the rule.
4. A test in `tests/test_scan.py`.

## Retire a tell

Taste moves. If a tell no longer signals generated output, open an issue with evidence. Retired tells move to a "Retired" section at the bottom of `SKILL.md` with the date and reason, keeping their number.

## Fix a false positive or false negative

Open a "Scanner accuracy" issue with the smallest snippet that reproduces it. In the fix, add the snippet to `tests/fixtures/clean.html` (false positive) or `tests/fixtures/vibecoded.html` (false negative) so it stays fixed.

## Ground rules

Keep the scanner dependency-free (Python standard library only). Run `python -m unittest discover tests` before opening a pull request. Write in plain language and skip em dashes, since the skill tells agents to avoid them and the repo should practice what it preaches. Never add advice that encourages fabricated social proof or placeholder legal text presented as final.
