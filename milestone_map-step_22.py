# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: MilestoneMap
def check_overdue_reminders(milestones):
    """Return a list of milestones whose reminders are past the deadline."""
    import datetime as dt
    now = dt.datetime.now()
    overdue = []
    for ms in milestones:
        if not hasattr(ms, 'reminder_deadline'):
            continue
        try:
            d = dt.datetime.strptime(ms.reminder_deadline, '%Y-%m-%d')
        except (ValueError, TypeError):
            continue
        if now > d:
            overdue.append({
                'name': ms.get('name', str(ms)),
                'deadline': ms.reminder_deadline,
                'status': ms.get('status', 'unknown'),
            })
    return overdue

# Пример использования в конце файла:
if __name__ == '__main__':
    sample = [
        {'name': 'Дизайн UI', 'reminder_deadline': '2025-12-31', 'status': 'done'},
        {'name': 'Бэкенд API', 'reminder_deadline': '2026-01-15', 'status': 'in_progress'},
    ]
    print(check_overdue_reminders(sample))  # покажет просроченные этапы
