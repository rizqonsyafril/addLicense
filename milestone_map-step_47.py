# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: MilestoneMap
def demo():
    print("=" * 50)
    print(" MilestoneMap — Демонстрация проекта")
    print("=" * 50)
    print()

    milestones = [
        {"id": "M1", "name": "Инициализация проекта", "owner": "PM",
         "start": "2024-01-01", "end": "2024-01-15", "progress": 100},
        {"id": "M2", "name": "Проектирование архитектуры", "owner": "Lead",
         "start": "2024-01-16", "end": "2024-02-28", "progress": 95},
        {"id": "M3", "name": "Разработка ядра", "owner": "Dev",
         "start": "2024-02-01", "end": "2024-04-30", "progress": 80},
        {"id": "M4", "name": "Тестирование", "owner": "QA",
         "start": "2024-03-01", "end": "2024-05-15", "progress": 60},
        {"id": "M5", "name": "Запуск в продакшн", "owner": "PM",
         "start": "2024-05-01", "end": "2024-06-30", "progress": 30},
    ]

    print("📋 Список этапов:")
    for m in milestones:
        bar = "█" * int(m["progress"] / 5) + "░" * (20 - int(m["progress"] / 5))
        print(f"  {m['id']}: {m['name']} [{bar}] {m['progress']}%")
    print()

    print("📊 Итоговая прогрессия проекта:")
    total = sum(m["progress"] for m in milestones)
    avg = total / len(milestones)
    print(f"  Средний прогресс: {avg:.1f}%")
    print(f"  Общий прогресс:   {total:.1f}%")
    print()

    print("✅ Демо завершено.")
