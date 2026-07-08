# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: MilestoneMap
def save_milestones(milestones, filepath="milestones.json"):
    import json
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump({"milestones": milestones, "count": len(milestones)}, f, ensure_ascii=False, indent=2)
