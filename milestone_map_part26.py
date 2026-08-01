# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: MilestoneMap
def demo_quick_test():
    """Демо: показать, что карта этапов работает."""
    print("=== Демо MilestoneMap ===")
    print(f"Сколько этапов в карте? {len(milestones)}")
    
    # Показываем первые 3 этапа (или все если их меньше)
    count = min(3, len(milestones))
    for i in range(count):
        m = milestones[i]
        print(f"Этап {i+1}: {m['name']}")
        
        # Показываем ответственного и срок
        if 'owner' in m:
            owner_info = f", ответственный: {m['owner']}"
        else:
            owner_info = ", ответственный: не назначен"
        
        if 'due_date' in m:
            date_info = f", срок: {m['due_date']}"
        else:
            date_info = ", срок: не установлен"
        
        print(f"{owner_info}{date_info}")

    # Показываем зависимости для первого этапа (если есть)
    if milestones and 'dependencies' in milestones[0]:
        deps = milestones[0]['dependencies']
        if isinstance(deps, list):
            for dep in deps:
                print(f"  Зависимость: {dep}")

if __name__ == "__main__":
    demo_quick_test()
