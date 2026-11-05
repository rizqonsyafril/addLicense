# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: MilestoneMap
print("=" * 48)
print("  MilestoneMap — финальная самопроверка")
print("=" * 48)
if not milestones:
    print("\n[ERROR] список этапов пуст — проект не инициализирован")
    raise SystemExit(1)
total = len(milestones)
done = sum(1 for m in milestones if m["status"] == "done")
in_progress = sum(1 for m in milestones if m["status"] == "in_progress")
blocked = sum(1 for m in milestones if m["status"] == "blocked")
ready = sum(1 for m in milestones if m["status"] == "done")
print(f"Всего этапов: {total}")
print(f"Готовы:       {done}")
print(f"В работе:     {in_progress}")
print(f"Блокированы:  {blocked}")
print(f"Готовность:   {round(done/total*100)}%")
ok = (done == total) and not blocked
if ok:
    print("\n[OK] Все этапы готовы, блокировок нет — проект завершён")
else:
    print("\n[TODO] Проект не завершён — остаются активные/блокированные этапы")
for m in milestones:
    if m["status"] in ("in_progress", "blocked"):
        print(f"  • [{m['status']}] {m['name']} — {m['owner']}")
if not ok:
    raise SystemExit(2)
