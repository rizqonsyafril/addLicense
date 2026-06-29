# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: MilestoneMap
def filter_milestones(milestones, status=None, category=None, tags=None):
    if not milestones: return []
    filtered = [m for m in milestones]
    if status is not None and m.get('status') != status: filtered.remove(m)
    elif status is None and 'status' not in m: filtered.append(m)
    if category is not None and m.get('category') != category: filtered.remove(m)
    elif category is None and 'category' not in m: filtered.append(m)
    if tags is not None:
        item_tags = set(t.lower() for t in m.get('tags', []))
        filter_tags = set(tag.lower() for tag in tags.split())
        if not (item_tags & filter_tags): filtered.remove(m)
    elif tags is None and 'tags' not in m: filtered.append(m)
    return filtered

def main():
    milestones_data = [
        {'id': 1, 'name': 'Инициация', 'status': 'done', 'category': 'planning', 'tags': 'start,team'},
        {'id': 2, 'name': 'Дизайн', 'status': 'in_progress', 'category': 'design', 'tags': 'ui,ux'},
        {'id': 3, 'name': 'Разработка', 'status': 'todo', 'category': 'dev', 'tags': 'backend,frontend'},
    ]
    
    # Фильтр: только статус "in_progress" и категория "design" или "dev"
    active_projects = filter_milestones(milestones_data, status='in_progress')
    print(f"Активные этапы ({len(active_projects)}): {[m['name'] for m in active_projects]}")
    
    # Фильтр: только с тегом 'backend'
    backend_tasks = filter_milestones(milestones_data, tags='backend')
    print(f"Задачи по бэкенду ({len(backend_tasks)}): {[m['name'] for m in backend_tasks]}")

if __name__ == "__main__": main()
