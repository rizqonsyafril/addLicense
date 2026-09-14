# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: MilestoneMap
def dry_run_mode(enabled: bool = True) -> None:
    global _DRY_RUN
    _DRY_RUN = enabled
    if enabled:
        print(f"[DRY-RUN] режим установлен: все операции изменения будут отменены.")
    else:
        print("[DRY-RUN] режим отключен.")
