from task_manager.task_manager import add_task, list_tasks, update_task, delete_task

# Добавление задачи
add_task("Позвонить другу", "Обсудить проект")

# Обновление задачи
update_task(1, title="Купить продукты и воду")

# Удаление задачи
# delete_task(2)

# Просмотр задач
print(list_tasks())
