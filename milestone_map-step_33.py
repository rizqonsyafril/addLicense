# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: MilestoneMap
def revert_last(self):
        """Откат последнего добавленного Milestone.
        Удаляет последнюю запись из списка и возвращает её."""
        if not self.milestones:
            print("Нет ничего для отката.")
            return None
        removed = self.milestones.pop()
        print(f"Откат: Milestone '{removed.name}' удалён.")
        return removed
