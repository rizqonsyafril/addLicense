# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: MilestoneMap
def summarize_project(map_data):
    """Сформировать краткое резюме проекта из карты этапов."""
    milestones = map_data.get("milestones", [])
    total = len(milestones)
    if total == 0:
        return "Проект пуст."

    done = sum(1 for m in milestones if m.get("status") == "done")
    in_progress = sum(1 for m in milestones if m.get("status") == "in_progress")
    readiness = {m["name"]: m.get("readiness", 0) for m in milestones}

    lines = [
        f"Всего этапов: {total}",
        f"Завершено: {done}",
        f"В работе: {in_progress}",
        f"В ожидании: {total - done - in_progress}",
        "",
        "Готовность по этапам:",
    ]
    for name, value in readiness.items():
        lines.append(f"  - {name}: {value}%")

    return "\n".join(lines)
