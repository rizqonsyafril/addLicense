# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: MilestoneMap
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

@dataclass
class Milestone:
    id: int
    name: str
    owner: str
    start_date: date
    end_date: date
    dependencies: List[int] = field(default_factory=list)
    readiness_percent: float = 0.0

def get_demo_data() -> List[Milestone]:
    return [
        Milestone(1, "Инициация", "Алексей", date(2024, 1, 1), date(2024, 1, 15)),
        Milestone(2, "Проектирование", "Мария", date(2024, 1, 16), date(2024, 2, 1), dependencies=[1]),
        Milestone(3, "Разработка ядра", "Иван", date(2024, 2, 2), date(2024, 3, 15), dependencies=[2]),
        Milestone(4, "Тестирование", "Мария", date(2024, 3, 16), date(2024, 4, 1), dependencies=[2, 3]),
    ]

if __name__ == "__main__":
    milestones = get_demo_data()
    for m in milestones:
        print(f"{m.id}: {m.name} ({m.owner}) [{m.start_date.date()} - {m.end_date.date()}] Ready: {m.readiness_percent}%")
