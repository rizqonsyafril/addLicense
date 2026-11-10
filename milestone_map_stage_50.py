# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: MilestoneMap
def _pct(value: float) -> str:
    return f"{value:.1f}%"


def _phase_status(m: Milestone) -> str:
    if m.done:
        return "Готов"
    if not m.deadline and not m.metrics:
        return "Черновик"
    if m.deadline and m.deadline < date.today():
        return "Просрочен"
    return "В работе"


def _progress_bar(m: Milestone, width: int = 12) -> str:
    done = min(m.progress, 100)
    filled = round(done / 100 * width)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def _metrics_row(m: Milestone) -> str:
    parts = []
    for key, value in m.metrics.items():
        label = key.replace("_", " ").title()
        parts.append(f"{label}: {_pct(value)}")
    return " | ".join(parts)


def _format_deadline(d: date | None) -> str:
    return d.strftime("%d.%m.%Y") if d else "—"


def _format_owner(name: str | None) -> str:
    return name if name else "—"


def print_milestone_card(m: Milestone) -> None:
    print()
    print(f"Этап {m.id}: {_pct(m.progress)}")
    print(f"Название: {m.title}")
    print(f"Ответственный: {_format_owner(m.owner)}")
    print(f"Срок: {_format_deadline(m.deadline)}")
    print(f"Статус: {_phase_status(m)}")
    print(f"Прогресс: {_progress_bar(m)}")
    if m.metrics:
        print(f"Показатели: {_metrics_row(m)}")
    print("-" * 40)


def print_project_map(milestones: list[Milestone]) -> None:
    print()
    print("Карта этапов проекта")
    print("=" * 40)
    for m in milestones:
        print_milestone_card(m)
    print("Готовность проекта:", _pct(sum(m.progress for m in milestones) / len(milestones) if milestones else 0))
