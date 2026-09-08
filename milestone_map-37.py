# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: MilestoneMap
import unittest

class TestMilestone(unittest.TestCase):
    def test_milestone_creation(self):
        m = Milestone("Design", "2024-01-15", "2024-02-15", "Alice", 50)
        self.assertEqual(m.name, "Design")
        self.assertEqual(m.responsible, "Alice")
        self.assertEqual(m.progress, 50)

    def test_milestone_completion(self):
        m = Milestone("Build", "2024-03-01", "2024-03-31", "Bob", 0)
        m.complete()
        self.assertTrue(m.is_completed)
        self.assertEqual(m.progress, 100)

    def test_milestone_dependency(self):
        dep = Milestone("Plan", "2024-01-01", "2024-01-31", "Charlie", 100)
        dep.complete()
        m = Milestone("Execute", "2024-02-01", "2024-02-28", "Charlie", 0, dependencies=[dep])
        m.check_dependencies()
        self.assertTrue(m.dependencies_met)

    def test_milestone_not_ready(self):
        dep = Milestone("Plan", "2024-01-01", "2024-01-31", "Charlie", 50)
        m = Milestone("Execute", "2024-02-01", "2024-02-28", "Charlie", 0, dependencies=[dep])
        m.check_dependencies()
        self.assertFalse(m.dependencies_met)

if __name__ == '__main__':
    unittest.main()
