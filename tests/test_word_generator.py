from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import word_generator


class WordGeneratorTests(unittest.TestCase):
    def test_initialize_creates_unique_words(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "words.json"

            data = word_generator.initialize_words(count=25, path=path, seed="test")
            words = [item["word"] for item in data["words"]]

            self.assertEqual(len(words), 25)
            self.assertEqual(len(words), len(set(words)))
            self.assertTrue(path.exists())

    def test_daily_add_is_idempotent_for_same_date(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "words.json"
            word_generator.initialize_words(count=5, path=path, seed="initial")
            now = datetime(2026, 6, 12, 20, 0, tzinfo=ZoneInfo("Europe/London"))

            changed_first, _, data_first = word_generator.add_daily_word(path=path, now=now, seed="daily")
            changed_second, _, data_second = word_generator.add_daily_word(path=path, now=now, seed="daily")

            self.assertTrue(changed_first)
            self.assertFalse(changed_second)
            self.assertEqual(len(data_first["words"]), 6)
            self.assertEqual(len(data_second["words"]), 6)

    def test_required_hour_skips_without_changing_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "words.json"
            word_generator.initialize_words(count=5, path=path, seed="initial")
            before = json.loads(path.read_text(encoding="utf-8"))
            now = datetime(2026, 6, 12, 19, 0, tzinfo=ZoneInfo("Europe/London"))

            changed, message, _ = word_generator.add_daily_word(
                path=path,
                now=now,
                require_local_hour=20,
            )
            after = json.loads(path.read_text(encoding="utf-8"))

            self.assertFalse(changed)
            self.assertIn("Skipped", message)
            self.assertEqual(before["words"], after["words"])


if __name__ == "__main__":
    unittest.main()
