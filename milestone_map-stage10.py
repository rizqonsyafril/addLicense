# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: MilestoneMap
import json


def export_milestone_map(data):
    """Export the current MilestoneMap state to a JSON string."""
    return json.dumps(data, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    # Example: create some sample data and export it
    sample_data = {
        "milestones": [
            {"id": 1, "name": "Planning", "status": "done", "owner": "Alice"},
            {"id": 2, "name": "Design", "status": "in_progress", "owner": "Bob"},
            {"id": 3, "name": "Development", "status": "pending", "owner": "Charlie"},
        ]
    }

    json_output = export_milestone_map(sample_data)
    print(json_output)
