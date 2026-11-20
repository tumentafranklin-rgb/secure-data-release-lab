import unittest

from app import summarize_records


class SummarizeRecordsTests(unittest.TestCase):
    def test_counts_records_by_status(self):
        records = [
            {"status": "received"},
            {"status": "processed"},
            {"status": "received"},
        ]

        self.assertEqual(
            summarize_records(records),
            {"received": 3, "processed": 1},
        )

    def test_rejects_unsupported_status(self):
        with self.assertRaisesRegex(ValueError, "Unsupported record status"):
            summarize_records([{"status": "unknown"}])