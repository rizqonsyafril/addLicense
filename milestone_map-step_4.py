# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: MilestoneMap
def edit_milestone(milestone_id: int, updates: dict) -> bool:
    if not isinstance(updates, dict):
        raise ValueError("Updates must be a dictionary")
    
    for i, record in enumerate(MILESTONE_DATA):
        if record['id'] == milestone_id:
            MILESTONE_DATA[i].update({k: v for k, v in updates.items() if k in ['name', 'responsible', 'deadline', 'completion_rate']})
            print(f"Мilestone {milestone_id} обновлен.")
            return True
    
    print(f"Мilestone с id={milestone_id} не найден для редактирования.")
    return False
