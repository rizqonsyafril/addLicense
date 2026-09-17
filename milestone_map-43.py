# === Stage 43: Добавь пагинацию длинных списков ===
# Project: MilestoneMap
class MilestoneMap:
    def __init__(self):
        self.milestones = {}

    def add(self, id, name, responsible, deadline, done=0):
        self.milestones[id] = {'name': name, 'responsible': responsible, 'deadline': deadline, 'done': done}
        return self

    def show(self, page=1, per_page=10):
        items = list(self.milestones.values())
        total = len(items)
        if total == 0:
            return {'page': page, 'total': 0, 'items': [], 'total_pages': 0}
        start = (page - 1) * per_page
        end = start + per_page
        page_items = items[start:end]
        return {'page': page, 'total': total, 'items': page_items, 'total_pages': (total + per_page - 1) // per_page}

    def done(self, ids, done=1):
        for id in ids:
            if id in self.milestones:
                self.milestones[id]['done'] = done
        return self
