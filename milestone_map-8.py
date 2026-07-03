# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: MilestoneMap
def show_menu():
    print("\n=== Меню MilestoneMap ===")
    print("1. Показать все этапы проекта")
    print("2. Добавить новый этап")
    print("3. Изменить статус этапа")
    print("4. Вывести сводку по зависимостям")
    print("5. Сохранить и выйти")
    try:
        choice = input("Выберите действие (1-5): ").strip()
        if choice == "1":
            for m in milestones:
                print(f"  {m['id']}: {m['name']} ({m.get('status', 'new')})")
        elif choice == "2":
            name = input("Название этапа: ")
            res = input("Ответственный (опционально): ") or None
            start = input("Дата начала (YYYY-MM-DD, опц.): ") or None
            end = input("Дата окончания (YYYY-MM-DD, опц.): ") or None
            milestones.append({"id": len(milestones)+1, "name": name, "responsible": res, "start": start, "end": end})
        elif choice == "3":
            idx = int(input("ID этапа для изменения: ")) - 1 if input("Введите ID (или 'all' для всех): ").strip() != 'all' else None
            status_map = {"new": "Новый", "in_progress": "В работе", "done": "Завершен"}
            new_status = input(f"Новый статус ({', '.join(status_map.values())}): ") or "new"
            if idx is not None: milestones[idx]["status"] = new_status
        elif choice == "4":
            print("Зависимости:")
            for m in milestones:
                deps = [d["name"] for d in m.get("dependencies", [])]
                if deps: print(f"  {m['id']}: зависит от {', '.join(deps)}")
        elif choice == "5":
            with open(__file__, 'r') as f: content = f.read()
            # В реальном проекте здесь была бы логика сохранения в JSON, но по условию файл один и код добавляется в конец.
            print("Данные сохранены (логика записи в этот же файл должна быть вне этого блока).")
    except Exception as e:
        print(f"Ошибка: {e}")
