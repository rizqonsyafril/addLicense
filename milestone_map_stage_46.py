# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: MilestoneMap
import pickle

MIGRATION_VERSION = 2

def migrate_v1_to_v2(data):
    if MIGRATION_VERSION in data:
        print("Already migrated.")
        return
    data[MIGRATION_VERSION] = MIGRATION_VERSION
    print("Migrated to v2.")
