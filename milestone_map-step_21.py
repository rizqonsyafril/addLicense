# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: MilestoneMap
import datetime


def add_reminders(data):
    today = data.get("today", "2026-05-15")
    for entry in data["milestones"]:
        deadline = entry.get("deadline") or entry.get("date")
        if deadline and not entry.get("reminder_added"):
            days_left = (datetime.date.fromisoformat(deadline) - datetime.date.fromisoformat(today)).days
            entry["reminder"] = "⏰" if days_left <= 1 else f"→ {days_left} дней до срока"
            entry["reminder_added"] = True

    return data


def print_reminders(data):
    today = data.get("today", "2026-05-15")
    urgent = []
    normal = []
    for entry in data["milestones"]:
        deadline = entry.get("deadline") or entry.get("date")
        if not deadline: continue
        days_left = (datetime.date.fromisoformat(deadline) - datetime.date.fromisoformat(today)).days
        if days_left <= 0:
            urgent.append((entry, f"СРОЧНО! Срок прошёл {abs(days_left)} дн. назад"))
        elif days_left <= 7:
            normal.append((entry, f"Внимание! Осталось {days_left} дней"))

    if urgent:
        print("🔴 Срочные напоминания:")
        for entry, msg in urgent:
            print(f"   • {entry['name']}: {msg}")
    if normal:
        print("\n🟡 Предстоящие напоминания:")
        for entry, msg in normal:
            print(f"   • {entry['name']}: {msg}")
