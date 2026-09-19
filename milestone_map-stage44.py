# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: MilestoneMap
def backup_data_file(filepath, backup_dir=".backups"):
    """Создаёт резервную копию файла данных в директории .backups с учётом существующих бэкапов."""
    import os, shutil
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(filepath)}_{timestamp}.bak")
    shutil.copy2(filepath, backup_path)
    return backup_path
