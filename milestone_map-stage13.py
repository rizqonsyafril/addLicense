# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: MilestoneMap
def search_milestones(query, fields=None):
    """Поиск по нескольким полям без учёта регистра."""
    if not query:
        return milestones
    if fields is None:
        fields = ['name', 'description', 'owner']
    q_lower = query.lower()
    for m in milestones:
        if any(q_lower in str(m[f]).lower() for f in fields):
            yield m
