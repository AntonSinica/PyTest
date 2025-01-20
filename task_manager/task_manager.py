import json
import os
import logging
from typing import List, Dict, Optional, Union

# Настройка логирования с указанием кодировки
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("task_manager.log", encoding="utf-8"),  # Указываем кодировку
        logging.StreamHandler()  # Логи будут выводиться в консоль
    ]
)


def load_tasks() -> List[Dict[str, Union[str, int]]]:
    """
    Загружает задачи из файла tasks.json.

    Возвращает:
        list: Список задач. Если файл не существует, возвращает пустой список.
    """
    if not os.path.exists("tasks.json"):
        return []
    with open("tasks.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks: List[Dict[str, Union[str, int]]]) -> None:
    """
    Сохраняет задачи в файл tasks.json.

    Аргументы:
        tasks (list): Список задач для сохранения.
    """
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def add_task(title: str, description: str) -> Dict[str, Union[str, int]]:
    """
    Добавляет новую задачу.

    Аргументы:
        title (str): Заголовок задачи. Не может быть пустым.
        description (str): Описание задачи.

    Возвращает:
        dict: Добавленная задача.

    Исключения:
        ValueError: Если заголовок пустой.
    """
    if not title:
        logging.error("Попытка добавить задачу с пустым заголовком")
        raise ValueError("Заголовок задачи не может быть пустым.")

    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {"id": task_id, "title": title, "description": description}
    tasks.append(new_task)
    save_tasks(tasks)
    logging.info(f"Добавлена новая задача: {new_task}")
    return new_task


def list_tasks() -> List[Dict[str, Union[str, int]]]:
    """
    Возвращает список всех задач.

    Возвращает:
        list: Список задач.
    """
    return load_tasks()


def update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Dict[
    str, Union[str, int]]:
    """
    Обновляет задачу по ID.

    Аргументы:
        task_id (int): ID задачи для обновления.
        title (str, optional): Новый заголовок задачи.
        description (str, optional): Новое описание задачи.

    Возвращает:
        dict: Обновлённая задача.

    Исключения:
        ValueError: Если задача с указанным ID не найдена.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if title:
                logging.info(f"Обновление заголовка задачи {task_id}: {task['title']} -> {title}")
                task["title"] = title
            if description:
                logging.info(f"Обновление описания задачи {task_id}: {task['description']} -> {description}")
                task["description"] = description
            save_tasks(tasks)
            return task
    logging.error(f"Задача с ID {task_id} не найдена.")
    raise ValueError(f"Задача с ID {task_id} не найдена.")


def delete_task(task_id: int) -> None:
    """
    Удаляет задачу по ID.

    Аргументы:
        task_id (int): ID задачи для удаления.

    Исключения:
        ValueError: Если задача с указанным ID не найдена.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            logging.info(f"Удалена задача: {task}")
            return
    logging.error(f"Задача с ID {task_id} не найдена.")
    raise ValueError(f"Задача с ID {task_id} не найдена.")
