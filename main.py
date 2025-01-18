from task_manager import add_task, list_tasks, update_task, delete_task

# Добавление задачи
add_task("Позвонить другу", "Обсудить проект")

# Просмотр задач
print(list_tasks())

# # Обновление задачи
# update_task(1, title="Купить продукты и воду")
#
# # Удаление задачи
# delete_task(2)