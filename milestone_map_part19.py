# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: MilestoneMap
def archive_completed(milestones, age_days=365):
    """Archive milestones that are completed or older than `age_days`."""
    now = datetime.now()
    archived = []
    for ms in milestones:
        if ms["status"] == "completed" or (now - ms["created_at"]).days > age_days:
            archived.append(ms)
    return archived
