import tempfile
import os
from repositories.task_repository import TaskRepository
from models.task import Task


def test_add_and_get_task():
    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = os.path.join(temp_dir, "tasks.json")
        repo = TaskRepository(filepath=filepath)

        task = Task(titulo="Teste Repo")
        repo.add(task)

        tasks = repo.get_all()

        assert len(tasks) == 1
        assert tasks[0].titulo == "Teste Repo"


def test_delete_task():
    with tempfile.TemporaryDirectory() as temp_dir:
        filepath = os.path.join(temp_dir, "tasks.json")
        repo = TaskRepository(filepath=filepath)

        task = Task(titulo="Excluir")
        repo.add(task)

        success = repo.delete(task.id)

        assert success is True
        assert repo.get_all() == []