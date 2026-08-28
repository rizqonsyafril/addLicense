# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: MilestoneMap
def switch_active_profile(user_profiles, active_profile_name):
    """Переключает активный профиль: ищет по имени и обновляет список."""
    active_profile_name = active_profile_name.lower()
    for profile in user_profiles:
        if profile["name"].lower() == active_profile_name:
            profile["active"] = True
            for other in user_profiles:
                if other is not profile:
                    other["active"] = False
            return profile
    raise ValueError(f"Профиль '{active_profile_name}' не найден среди пользователей.")
