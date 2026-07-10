# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: MilestoneMap
def load_milestones_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [Milestone(m['name'], m.get('description',''), m['owner'], m['start_date'], m['end_date'], m['status']) for m in data]
        elif isinstance(data, dict):
            return [Milestone(data.get('name',''), data.get('description',''), data.get('owner',''), data.get('start_date',''), data.get('end_date',''), data.get('status','in_progress'))]
        else:
            raise ValueError("Unsupported JSON format")
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
    except KeyError as e:
        print(f"Пропущены обязательные поля в данных: {e}")
        return []

if __name__ == '__main__':
    milestones = load_milestones_from_json('milestones.json')
    if milestones:
        for m in milestones:
            print(m)
