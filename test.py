# Supplied checks for your program.
#
# Run from this folder:
#
#     python3 test.py -v
#
# These checks fail until Museum.py runs and prints the expected nine lines for
# each one. They do NOT cover everything your program must handle: designing
# your own test cases (up to ten, in tests.txt) is a separate, graded part of
# the assignment -- see "Testing your program" in brief.md. Predict
# every expected output by reasoning about the rules before you run anything.
#
# What you should see:
#
# - ALL checks passing ends with:
#
#       ----------------------------------------------------------------------
#       Ran 3 tests in ...s
#
#       OK
#
# - If SOME checks fail, each failed one is listed under "FAIL:" with a diff
#   between what your program printed and what was expected; the run ends with
#   "FAILED (failures=N)". (With the untouched skeleton you will see an error
#   for every test, because the ??? placeholders are not valid Python.)
#
# Fix the first failing case and re-run; repeat until you get "OK".

import subprocess
import sys
import unittest
from pathlib import Path

PROGRAM = Path(__file__).resolve().parent / "Museum.py"

EXAMPLE_1_INPUT = "1\n5\n30\n-1\n"
EXAMPLE_1_OUTPUT = [
    "Day type: weekday",
    "Children: 1",
    "Adults: 1",
    "Seniors: 0",
    "Total people: 2",
    "Groups formed: 0",
    "Discount: 0.00",
    "Service fee: 0.00",
    "Total cost: 90.00",
]

EXAMPLE_2_INPUT = "1\n30\n30\n30\n30\n30\n30\n65\n65\n8\n8\n-1\n"
EXAMPLE_2_OUTPUT = [
    "Day type: weekday",
    "Children: 2",
    "Adults: 6",
    "Seniors: 2",
    "Total people: 10",
    "Groups formed: 1",
    "Discount: 0.00",
    "Service fee: 30.00",
    "Total cost: 405.00",
]

EXAMPLE_3_INPUT = "6\n30\n30\n30\n30\n30\n30\n65\n65\n8\n8\n-1\n"
EXAMPLE_3_OUTPUT = [
    "Day type: weekend",
    "Children: 2",
    "Adults: 6",
    "Seniors: 2",
    "Total people: 10",
    "Groups formed: 1",
    "Discount: 58.50",
    "Service fee: 30.00",
    "Total cost: 556.50",
]


class WorkedExampleTests(unittest.TestCase):
    def check(self, stdin_text, expected_lines):
        if not PROGRAM.exists():
            self.fail(f"Museum.py not found next to test.py (looked at {PROGRAM})")
        result = subprocess.run(
            [sys.executable, str(PROGRAM)],
            input=stdin_text,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            self.fail(
                "Museum.py crashed before producing output (it may still "
                "contain the ??? placeholders).\nstderr was:\n" + result.stderr
            )
        # input() echoes each prompt into stdout; strip the two known prompts
        # so only the program's own printed lines are compared.
        printed = (
            result.stdout
            .replace("Enter day (1-8): ", "")
            .replace("Enter age (-1 to stop): ", "")
        )
        self.assertEqual(
            printed.splitlines(),
            expected_lines,
            "Output did not match exactly (labels, spaces, and decimals count)",
        )

    def test_example_1_weekday_fee_waived(self):
        self.check(EXAMPLE_1_INPUT, EXAMPLE_1_OUTPUT)

    def test_example_2_weekday_group_capped_fee(self):
        self.check(EXAMPLE_2_INPUT, EXAMPLE_2_OUTPUT)

    def test_example_3_weekend_group_discount(self):
        self.check(EXAMPLE_3_INPUT, EXAMPLE_3_OUTPUT)


if __name__ == "__main__":
    unittest.main()
