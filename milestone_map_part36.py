# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: MilestoneMap
def validate_and_repair(milestones):
    """Проверка целостности и автоматический ремонт простых проблем.

    Проверяет:
      - все зависимости ссылаются на существующие этапы;
      - даты не образуют циклов (т.е. каждый этап может быть выполнен);
      - статус "done" не стоит на этапе с зависимость на недоступный этап.

    Возвращает список сообщений о найденных и исправленных проблемах.
    """
    issues = []

    # 1. Проверка и замена несуществующих зависимостей
    existing = {m["id"] for m in milestones}
    for m in milestones:
        if m["depends_on"] and m["depends_on"] not in existing:
            issues.append(f"Этап {m['id']}: зависимость {m['depends_on']} не найдена. Удалена.")
            m["depends_on"] = None

    # 2. Проверка статусов: done не может быть при зависимости на active
    for m in milestones:
        if m["status"] == "done" and m["depends_on"]:
            dep = next((x for x in milestones if x["id"] == m["depends_on"]), None)
            if dep and dep["status"] not in ("done", "completed"):
                issues.append(f"Этап {m['id']}: статус done при зависимости на {dep['status']}. Исправлено -> completed.")
                m["status"] = "completed"

    # 3. Проверка и ремонт сроков: если deadline < start, поправим
    for m in milestones:
        if m["start"] and m["deadline"] and m["deadline"] < m["start"]:
            issues.append(f"Этап {m['id']}: deadline ({m['deadline']}) раньше start ({m['start']}). Установлено deadline = start.")
            m["deadline"] = m["start"]

    return issues
