# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: MilestoneMap
import unittest
from datetime import datetime

class TestMilestoneMapEdgeCases(unittest.TestCase):
    def test_empty_project(self):
        from src.milestonemap import MilestoneMap
        mm = MilestoneMap()
        mm.add_milestone("Init", "dev", "2024-01-01", 100)
        mm.add_milestone("Plan", "dev", "2024-01-05", 80)
        mm.add_milestone("Done", "dev", "2024-01-10", 100)
        self.assertEqual(mm.status(), "Completed")

    def test_invalid_dates(self):
        from src.milestonemap import MilestoneMap
        mm = MilestoneMap()
        with self.assertRaises(ValueError):
            mm.add_milestone("Bad", "dev", "not-a-date", 50)

    def test_out_of_order_dates(self):
        from src.milestonemap import MilestoneMap
        mm = MilestoneMap()
        mm.add_milestone("First", "dev", "2024-01-10", 60)
        mm.add_milestone("Second", "dev", "2024-01-01", 70)
        self.assertEqual(mm.status(), "WIP")

    def test_zero_progress(self):
        from src.milestonemap import MilestoneMap
        mm = MilestoneMap()
        mm.add_milestone("Not started", "dev", "2024-02-01", 0)
        self.assertEqual(mm.status(), "WIP")

    def test_over_100_progress(self):
        from src.milestonemap import MilestoneMap
        mm = MilestoneMap()
        mm.add_milestone("Done+10", "dev", "2024-02-01", 110)
        self.assertEqual(mm.status(), "Completed")

if __name__ == "__main__":
    unittest.main()
