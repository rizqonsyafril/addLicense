# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: MilestoneMap
APP_CONFIG = {
    "app_name": "MilestoneMap",
    "app_version": "0.1",
    "app_description": "Карта этапов проекта с зависимостями, ответственными, сроками и показателями готовности",
    "app_author": "Ornith",
    "app_license": "MIT",
    "app_year": 2024,
    "milestones": {
        "m1": {"name": "Инициация", "owner": "PM", "deadline": "2024-01-15", "progress": 100},
        "m2": {"name": "Анализ", "owner": "Analyst", "deadline": "2024-01-20", "progress": 80},
        "m3": {"name": "Разработка", "owner": "Dev", "deadline": "2024-02-15", "progress": 60},
        "m4": {"name": "Тестирование", "owner": "QA", "deadline": "2024-03-01", "progress": 40},
        "m5": {"name": "Релиз", "owner": "Release", "deadline": "2024-03-15", "progress": 20},
    },
    "dependencies": {
        "m2": "m1",
        "m3": "m2",
        "m4": "m3",
        "m5": "m4",
    },
    "status": "active",
    "start_date": "2024-01-01",
    "end_date": "2024-03-15",
}
