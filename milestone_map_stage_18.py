# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: MilestoneMap
class Tag:
    def __init__(self, name):
        self.name = name.lower()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other.lower()
        if isinstance(other, Tag):
            return self.name == other.name
        return NotImplemented

    def __hash__(self):
        return hash(self.name)


class Project:
    def __init__(self, title):
        self.title = title
        self.milestones = []
        self.tags = set()

    def add_milestone(self, name, owner, start_date, end_date, dependencies=None, progress=0):
        ms = Milestone(name=name, owner=owner, start_date=start_date, end_date=end_date,
                       dependencies=dependencies or [], progress=progress)
        self.milestones.append(ms)
        return ms

    def add_tag(self, tag_name):
        if tag_name not in self.tags:
            self.tags.add(tag_name.lower())

    def remove_tag(self, tag_name):
        if tag_name.lower() in self.tags:
            self.tags.discard(tag_name.lower())

    def get_tags(self):
        return list(self.tags)
