# === Stage 20: Добавь восстановление записей из архива ===
# Project: MilestoneMap
import json, os

ARCHIVE_FILE = "milestones_archive.json"

def load_from_archive():
    if not os.path.exists(ARCHIVE_FILE):
        return []
    try:
        with open(ARCHIVE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "records" in data:
            return data["records"]
        return []
    except (json.JSONDecodeError, IOError):
        return []
