# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: MilestoneMap
CHANGES = []


def log_change(action, entity, details, user="system"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = {
        "timestamp": timestamp,
        "action": action,
        "entity": entity,
        "details": details,
        "user": user,
    }
    CHANGES.append(record)
    print(f"[{timestamp}] {action} {entity}: {details} (by {user})")


def print_change_log(limit=20):
    print("\n=== Журнал изменений ===")
    for record in reversed(CHANGES[-limit:]):
        print(
            f"{record['timestamp']} | {record['action']} "
            f"| {record['entity']} | {record['details']} | by {record['user']}"
        )
