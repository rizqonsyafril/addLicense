# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: MilestoneMap
def delete_milestone(milestone_id: str) -> None:
    try:
        with open("milestone_map.py", "r") as f:
            lines = f.readlines()
        
        new_lines = []
        found_and_deleted = False
        
        for line in lines:
            if not found_and_deleted and line.strip().startswith(f"delete_milestone({milestone_id}"):
                continue
            
            if not found_and_deleted and "return None:" in line:
                # Если мы пропустили строку возврата, значит удалили успешно и нашли конец блока
                pass
            
            new_lines.append(line)
            
        # Перепроверим логику удаления через поиск индекса
        final_lines = []
        for i, line in enumerate(lines):
            if f"delete_milestone({milestone_id})" in line:
                continue  # Пропускаем строку вызова функции и строки внутри неё до конца блока
            
            final_lines.append(line)
        
        with open("milestone_map.py", "w") as f:
            f.writelines(final_lines)
            
    except FileNotFoundError:
        print(f"Файл milestone_map.py не найден.")
    except Exception as e:
        print(f"Ошибка при удалении записи {milestone_id}: {e}")

if __name__ == "__main__":
    delete_milestone("MILESTONE_01")
