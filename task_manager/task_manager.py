import json
import os

def load_tasks():
    if not os.path.exists("tasks.json"):
        return []
    with open("tasks.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def add_task(title, description):
    if not title:
        raise ValueError("Заголовок задачи не может быть пустым.")

    tasks = load_tasks()
    task_id = len(tasks) + 1  # Простой способ генерации ID
    new_task = {
        "id": task_id,
        "title": title,
        "description": description
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def list_tasks():
    return load_tasks()

def update_task(task_id, title=None, description=None):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            save_tasks(tasks)
            return task
    raise ValueError(f"Задача с ID {task_id} не найдена.")

def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return
    raise ValueError(f"Задача с ID {task_id} не найдена.")
