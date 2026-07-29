# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: MilestoneMap
def print_milestone(m):
    if not m: return
    name = m.get('name','?')
    resp = m.get('owner','?')
    status = m.get('status','?')
    deadline = m.get('deadline','?')
    deps = m.get('deps',[])
    progress = m.get('progress',0)
    print(f"  [{name}]")
    print(f"      ответственный: {resp}")
    print(f"      статус:        {status}")
    print(f"      дедлайн:       {deadline}")
    if deps:
        print(f"      зависимости:   {', '.join(deps)}")
    print(f"      прогресс:      {progress}%")
