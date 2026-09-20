# === Stage 45: Добавь восстановление из резервной копии ===
# Project: MilestoneMap
import json
import shutil
from datetime import datetime

BACKUP_DIR = "milestone_backup"

def create_backup(milestones, dependencies, responsible, deadlines, readiness):
    """Создаёт резервную копию всех данных проекта."""
    backup_data = {
        "milestones": milestones,
        "dependencies": dependencies,
        "responsible": responsible,
        "deadlines": deadlines,
        "readiness": readiness,
        "backup_date": datetime.now().isoformat()
    }
    os.makedirs(BACKUP_DIR, exist_ok=True)
    filepath = os.path.join(BACKUP_DIR, f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(backup_data, f, ensure_ascii=False, indent=2)
    print(f"Резервная копия сохранена: {filepath}")
    return filepath

def restore_backup(backup_path):
    """Восстанавливает данные из резервной копии, заменяя текущие."""
    if not os.path.exists(backup_path):
        print(f"Файл резервной копии не найден: {backup_path}")
        return None
    with open(backup_path, "r", encoding="utf-8") as f:
        backup_data = json.load(f)
    milestones = backup_data["milestones"]
    dependencies = backup_data["dependencies"]
    responsible = backup_data["responsible"]
    deadlines = backup_data["deadlines"]
    readiness = backup_data["readiness"]
    backup_date = backup_data.get("backup_date", "неизвестно")
    print(f"Восстановлено из резервной копии от {backup_date}")
    print(f"Восстановлено {len(milestones)} этапов проекта")
    return {
        "milestones": milestones,
        "dependencies": dependencies,
        "responsible": responsible,
        "deadlines": deadlines,
        "readiness": readiness
    }
