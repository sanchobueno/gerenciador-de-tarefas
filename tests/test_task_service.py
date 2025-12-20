import tempfile
import os
import pytest
from repositories.task_repository import TaskRepository
from services.task_service import TaskService


def create_service():
    temp_dir = tempfile.TemporaryDirectory()
    filepath = os.path.join(temp_dir.name, "tasks.json")
    repo = TaskRepository(filepath=filepath)
    return TaskService(repo), temp_dir


def test_create_task_success():
    service, temp_dir = create_service()

    task = service.create_task("Nova tarefa")

    assert task.titulo == "Nova tarefa"
    assert task.status == "pendente"

    temp_dir.cleanup()


def test_create_task_with_empty_title_fails():
    service, temp_dir = create_service()

    with pytest.raises(ValueError):
        service.create_task("   ")

    temp_dir.cleanup()


def test_complete_task():
    service, temp_dir = create_service()

    task = service.create_task("Completar")
    completed = service.complete_task(task.id)

    assert completed.status == "concluida"

    temp_dir.cleanup()
