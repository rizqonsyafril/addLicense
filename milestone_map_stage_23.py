# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: MilestoneMap
def print_milestone_table(milestones):
    """Форматированный вывод таблицы этапов проекта в консоль."""
    if not milestones:
        print("Нет данных для отображения.")
        return

    # Вычисляем ширину колонок
    headers = ["ID", "Название", "Ответственный", "Срок", "Статус", "Прогресс"]
    col_widths = [len(h) for h in headers]
    
    for ms in milestones:
        if isinstance(ms, dict):
            row = (str(ms.get("id")), str(ms.get("name", "")), 
                   str(ms.get("owner", "")), str(ms.get("deadline", "")),
                   str(ms.get("status", "")), str(ms.get("progress", 0)))
        else:
            row = (str(ms[0]), str(ms[1] or ""), str(ms[3] or ""), 
                   str(ms[4] or ""), str(ms[5] or ""), str(ms[6] or ""))
        
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(val))

    # Заголовки
    print("─" * (sum(col_widths) + 3 * len(headers)))
    header_line = " │ ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_line)
    print("─" * (sum(col_widths) + 3 * len(headers)))

    # Строки данных
    for ms in milestones:
        if isinstance(ms, dict):
            row = [str(ms.get(f, "")) for f in ["id", "name", "owner", "deadline", "status", "progress"]]
        else:
            row = list(ms)
        
        line = " │ ".join(val.ljust(col_widths[i]) for i, val in enumerate(row))
        print(line)

    print("─" * (sum(col_widths) + 3 * len(headers)))
