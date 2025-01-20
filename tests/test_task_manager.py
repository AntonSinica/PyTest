import pytest
import os
from task_manager.task_manager import add_task, list_tasks, update_task, delete_task, load_tasks, save_tasks


@pytest.fixture
def setup_tasks():
    # Создаем временный файл tasks.json
    tasks = [
        {"id": 1, "title": "Купить продукты", "description": "Молоко, хлеб, яйца"},
        {"id": 2, "title": "Сделать домашку", "description": "Проект по Python"}
    ]
    save_tasks(tasks)
    yield  # Здесь выполняется тест
    # Удаляем временный файл после завершения теста
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")


def test_add_task(setup_tasks):
    # Проверка добавления новой задачи
    new_task = add_task("Позвонить другу", "Обсудить проект")
    assert new_task["title"] == "Позвонить другу"
    assert new_task["description"] == "Обсудить проект"
    assert new_task["id"] == 3  # ID должен быть следующим после существующих задач

    # Проверка, что задача добавлена в список
    tasks = list_tasks()
    assert len(tasks) == 3
    assert tasks[-1]["title"] == "Позвонить другу"

    # Проверка на пустой заголовок
    with pytest.raises(ValueError):
        add_task("", "Описание")


def test_list_tasks(setup_tasks):
    # Проверка, что список задач возвращается корректно
    tasks = list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Купить продукты"
    assert tasks[1]["description"] == "Проект по Python"

    # Проверка, что список пуст, если нет задач
    delete_task(1)
    delete_task(2)
    tasks = list_tasks()
    assert len(tasks) == 0


def test_update_task(setup_tasks):
    # Проверка обновления существующей задачи
    updated_task = update_task(1, title="Купить продукты и воду")
    assert updated_task["title"] == "Купить продукты и воду"

    # Проверка, что задача обновлена в списке
    tasks = list_tasks()
    assert tasks[0]["title"] == "Купить продукты и воду"

    # Проверка обновления несуществующей задачи
    with pytest.raises(ValueError):
        update_task(999, title="Несуществующая задача")


def test_delete_task(setup_tasks):
    # Проверка удаления существующей задачи
    delete_task(1)
    tasks = list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2

    # Проверка удаления несуществующей задачи
    with pytest.raises(ValueError):
        delete_task(999)


def test_load_tasks_file_not_exist():
    # Убедимся, что файл tasks.json не существует
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

    # Проверяем, что load_tasks возвращает пустой список
    tasks = load_tasks()
    assert tasks == []


def test_delete_task_not_found(setup_tasks):
    print("Запуск теста test_delete_task_not_found")
    with pytest.raises(ValueError) as exc_info:
        delete_task(999)  # ID, которого нет в списке
    assert str(exc_info.value) == "Задача с ID 999 не найдена."

def test_update_task_description_only(setup_tasks):
    # Обновляем только описание задачи
    updated_task = update_task(1, description="Молоко, хлеб, яйца, вода")
    assert updated_task["description"] == "Молоко, хлеб, яйца, вода"

    # Проверяем, что задача обновлена в списке
    tasks = list_tasks()
    assert tasks[0]["description"] == "Молоко, хлеб, яйца, вода"