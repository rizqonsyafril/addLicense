# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: MilestoneMap
import json


def export_report(milestones, path="milestone_report.txt"):
    lines = []
    lines.append("MILEstonESTONE MAP - краткий отчёт")
    lines.append("=" * 45)
    lines.append(f"Всего этапов: {len(milestones)}")
    done = sum(1 for m in milestones if m["ready"] >= 100)
    lines.append(f"Готовы: {done}/{len(milestones)}")
    lines.append(f"Общий прогресс: {round(done / len(milestones) * 100, 1)}%")
    lines.append("")
    lines.append("Этапы:")
    for m in milestones:
        resp = m.get("responsible", "-")
        due = m.get("due", "-")
        status = "готов" if m["ready"] >= 100 else ("в работе" if m["ready"] > 0 else "новый")
        lines.append(f"  - {m['name']} [{status}]")
        lines.append(f"      ответственный: {resp}, срок: {due}, готовность: {m['ready']}%")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path


def export_json(milestones, path="milestone_report.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(milestones, f, ensure_ascii=False, indent=2)
    return path
