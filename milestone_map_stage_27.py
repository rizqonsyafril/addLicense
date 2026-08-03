# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: MilestoneMap
def reset_demo_data():
    """Сбрасывает все данные в их демо-значения."""
    milestones = [
        {"id": 1, "name": "Проектирование", "status": "completed", "owner": "Архитектор", "start": "2025-03-01", "end": "2025-04-15"},
        {"id": 2, "name": "Разработка ядра", "status": "in_progress", "owner": "Backend", "start": "2025-04-16", "end": "2025-07-30"},
        {"id": 3, "name": "Frontend", "status": "pending", "owner": "UI Team", "start": "2025-07-01", "end": "2026-01-31"},
    ]
    dependencies = [(1, 2), (2, 3)]
    owners = {"Архитектор": 1, "Backend": 2, "UI Team": 3}
    readiness = {1: 95, 2: 40, 3: 0}

def clear_state():
    """Очищает все данные и сбрасывает статусы."""
    milestones = [
        {"id": i, "name": "", "status": "pending", "owner": "", "start": "", "end": ""}
        for i in range(1, 4)
    ]
    dependencies = []
    owners = {}
    readiness = {i: 0 for i in range(1, 4)}

if __name__ == "__main__":
    reset_demo_data()
    clear_state()
