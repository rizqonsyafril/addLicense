# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: MilestoneMap
class Milestone:
    def __init__(self, name, owner, start_date, end_date):
        self.name = name.strip()
        self.owner = owner.strip()
        self.start_date = start_date.strip()
        self.end_date = end_date.strip()
    
    @property
    def is_valid(self):
        if not all([self.name, self.owner]): return False
        try:
            from datetime import datetime
            s = datetime.strptime(self.start_date, "%Y-%m-%d")
            e = datetime.strptime(self.end_date, "%Y-%m-%d")
            return s <= e and len(self.name) < 50
        except ValueError:
            return False

def parse_milestone_input(raw_data):
    lines = [l.strip() for l in raw_data.splitlines()] if isinstance(raw_data, str) else []
    milestones = []
    for line in lines:
        parts = line.split(',')
        if len(parts) >= 4:
            try:
                m = Milestone(*parts[:4])
                if m.is_valid:
                    milestones.append(m)
            except Exception:
                continue
    return milestones
