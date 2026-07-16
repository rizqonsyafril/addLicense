# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: MilestoneMap
def weekly_stats(milestones):
    """Расчёт недельной статистики по датам."""
    from datetime import timedelta
    weeks = {}
    for ms in milestones:
        start = ms["start_date"]
        end = ms.get("end_date", start)
        current = start
        while current <= end:
            week_key = current.strftime("%Y-W%W")
            if week_key not in weeks:
                weeks[week_key] = {"completed": 0, "in_progress": 0, "pending": 0}
            status = ms["status"]
            if status == "done":
                weeks[week_key]["completed"] += 1
            elif status in ("active", "in_progress"):
                weeks[week_key]["in_progress"] += 1
            else:
                weeks[week_key]["pending"] += 1
            current += timedelta(weeks=1)
    return {k: dict(sorted(v.items())) for k, v in sorted(weeks.items())}
