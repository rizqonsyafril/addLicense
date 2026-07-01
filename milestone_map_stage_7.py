# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: MilestoneMap
def sort_milestones(milestones, key='date'):
    if not milestones: return []
    reverse = False
    if key == 'priority': reverse = True
    elif key == 'name': pass
    try:
        milestones.sort(key=lambda m: (m.get('completed', 0) > 0), reverse=False)
        milestones.sort(key=lambda m: m.get(key, ''), reverse=reverse)
    except TypeError:
        return sorted(milestones, key=lambda m: str(m.get(key, '')), reverse=reverse)
    return milestones
