# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: MilestoneMap
def monthly_stats():
    """Расчёт месячной статистики по датам"""
    stats = {}
    for m in milestones:
        if m.date:
            key = f"{m.date.year}-{m.date.month}"
            stats.setdefault(key, {"count": 0, "total_progress": 0})
            stats[key]["count"] += 1
            stats[key]["total_progress"] += round(m.progress * 100)
    return dict(sorted(stats.items()))
