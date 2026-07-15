# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: MilestoneMap
def generate_summary(milestones, dependencies):
    """Генерирует краткую сводку по текущим данным проекта."""
    summary = []
    total = len(milestones)
    if not total:
        return "Нет данных для сводки."

    statuses = {}
    for m in milestones:
        s = m.get('status', 'unknown')
        statuses[s] = statuses.get(s, 0) + 1
    
    summary.append(f"Итого этапов: {total}")
    for status, count in sorted(statuses.items()):
        summary.append(f"  статус '{status}': {count} этап(ов)")

    blocked = []
    completed_deps = set()
    for m in milestones:
        if 'deps' not in m or not m['deps']:
            continue
        deps_list = m['deps']
        if all(dep.get('id') in completed_deps for dep in deps_list):
            continue
        blocked.append(m.get('name', '?'))

    if blocked:
        summary.append(f"  заблокировано зависимостями: {', '.join(blocked)}")

    return '\n'.join(summary)
