# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: MilestoneMap
import json, ast

def load_milestones_from_json(json_string):
    try:
        data = json.loads(json_string)
        milestones = []
        for item in data.get("milestones", []):
            milestone = {
                "id": item["id"],
                "name": item["name"],
                "owner": item["owner"],
                "start_date": ast.literal_eval(item["start_date"]),
                "end_date": ast.literal_eval(item["end_date"]),
                "dependencies": [int(d) for d in item.get("dependencies", [])],
                "readiness_score": int(item.get("readiness_score", 0)),
            }
            milestones.append(milestone)
        return milestones
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return []

initial_data = '{"milestones":[{"id":1,"name":"Инициация","owner":"Алексей","start_date":[2024,1,1],"end_date":[2024,3,31],"dependencies":[],"readiness_score":85},{"id":2,"name":"Дизайн","owner":"Мария","start_date":[2024,2,1],"end_date":[2024,4,15],"dependencies":[1],"readiness_score":70}]}'.replace("'", '"')
milestones = load_milestones_from_json(initial_data)
