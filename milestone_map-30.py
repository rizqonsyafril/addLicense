# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: MilestoneMap
class Profile:
    def __init__(self, name, role, department):
        self.name = name
        self.role = role
        self.department = department
    def display(self):
        return f"Profile: {self.name} | Role: {self.role} | Department: {self.department}"

def add_profile_support(app):
    profiles = []
    def register_profile(name, role, department):
        p = Profile(name, role, department)
        profiles.append(p)
        print(f"Registered profile: {p.display()}")
    def list_profiles():
        if not profiles:
            print("No profiles registered yet.")
        else:
            for p in profiles:
                print(p.display())
    app.register_profile = register_profile
    app.list_profiles = list_profiles
    return app
