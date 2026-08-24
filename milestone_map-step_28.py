# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: MilestoneMap
def calculate_project_metrics(milestones):
    total = len(milestones)
    if total == 0:
        return {"completed": 0, "in_progress": 0, "pending": 0, "total": 0, "progress_percent": 0.0}
    completed = sum(1 for m in milestones if m["status"] == "completed")
    in_progress = sum(1 for m in milestones if m["status"] == "in_progress")
    pending = total - completed - in_progress
    progress_percent = round(completed / total * 100, 1)
    return {"completed": completed, "in_progress": in_progress, "pending": pending, "total": total, "progress_percent": progress_percent}
