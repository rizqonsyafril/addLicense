# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: MilestoneMap
class Template:
    def __init__(self, name, stage, owner, dependencies, duration, target):
        self.name = name
        self.stage = stage
        self.owner = owner
        self.dependencies = dependencies or []
        self.duration = duration
        self.target = target

    def apply(self, db, today):
        for t in db.templates:
            if t.name == self.name and t.stage == self.stage and t.owner == self.owner and t.dependencies == self.dependencies and t.duration == self.duration and t.target == self.target:
                return
            db.templates.append(self)

    def __repr__(self):
        return f"Template({self.name}, stage={self.stage}, owner={self.owner}, deps={self.dependencies}, days={self.duration}, target={self.target})"
