# === Stage 32: Добавь журнал действий пользователя ===
# Project: MilestoneMap
import json
from datetime import datetime

class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user, action, detail=""):
        self.entries.append({
            "timestamp": datetime.now().isoformat(),
            "user": user,
            "action": action,
            "detail": detail
        })

    def get_log(self):
        return self.entries

    def clear(self):
        self.entries.clear()

    def summary(self):
        return {
            "total_actions": len(self.entries),
            "users": list(set(e["user"] for e in self.entries)),
            "recent": self.entries[-5:]
        }
