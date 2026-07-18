# === Stage 17: Добавь группировку записей по категориям ===
# Project: MilestoneMap
def group_milestones_by_category(milestones, categories):
    grouped = {cat: [] for cat in categories}
    for ms in milestones:
        cat = ms.get("category") or "Uncategorized"
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(ms)
    return grouped
