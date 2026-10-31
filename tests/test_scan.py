import os
import sys
import unittest

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "vibecode-tells", "scripts"))
import scan  # noqa: E402

FIX = os.path.join(HERE, "fixtures")
EXPECTED_ON_VIBECODED = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                         19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


class ScanTests(unittest.TestCase):
    def test_vibecoded_fixture_flags_every_detectable_tell(self):
        hits = scan.scan(os.path.join(FIX, "vibecoded.html"))
        missing = [n for n in EXPECTED_ON_VIBECODED if n not in hits]
        self.assertEqual(missing, [], f"tells not detected: {missing}")

    def test_clean_fixture_flags_nothing(self):
        hits = scan.scan(os.path.join(FIX, "clean.html"))
        self.assertEqual(hits, {}, f"false positives: {sorted(hits)}")

    def test_decided_fixture_flags_nothing(self):
        hits = scan.scan(os.path.join(FIX, "decided.html"))
        self.assertEqual(hits, {}, f"false positives: {sorted(hits)}")


if __name__ == "__main__":
    unittest.main()
