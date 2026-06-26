# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: MilestoneMap
class MilestoneMap:
    def __init__(self):
        self._records = []

    def add_milestone(self, name, owner, deadline, readiness=0.0, dependencies=None):
        record = {
            "name": name,
            "owner": owner,
            "deadline": deadline,
            "readiness": float(readiness),
            "dependencies": list(dependencies) if dependencies else []
        }
        self._records.append(record)

    def get_all(self):
        return self._records.copy()
