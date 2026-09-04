# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: MilestoneMap
def get_next_actions(self, milestones: list[dict], now: datetime) -> list[str]:
        overdue = [m for m in milestones if m["deadline"] and m["deadline"] < now]
        if overdue:
            return [f"Срочно: {m['name']} просрочена (срок: {m['deadline'].strftime('%d.%m')})." for m in overdue]
        not_started = [m for m in milestones if m["status"] == "not_started"]
        if not_started:
            return [f"Планировать: {m['name']} — статус 'не начато'." for m in not_started]
        low_progress = [m for m in milestones if m["status"] == "in_progress" and m["progress"] < 50]
        if low_progress:
            return [f"Ускорить: {m['name']} — прогресс {m['progress']}%, нужно больше ресурсов." for m in low_progress]
        blocked = [m for m in milestones if m["status"] == "blocked"]
        if blocked:
            return [f"Разблокировать: {m['name']} — зависимость '{m.get('blocker', 'неизвестно')}'." for m in blocked]
        return ["Все этапы в норме. Следите за прогрессом." if milestones else "Нет этапов в проекте."]
