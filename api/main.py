from fastapi import FastAPI, Depends
from repositories.task_repository import TaskRepository
from services.task_service import TaskService
from typing import Optional

from schemas.task_filter import TaskFilter
from schemas.task_response import TaskResponse
from schemas.task_create import TaskCreate


repository = TaskRepository()
service = TaskService(repository)


app = FastAPI(
    title="Gerenciador de Tarefas API",
    description="API para gerenciar tarefas, permitindo criar, ler, atualizar e deletar tarefas.",
    version="1.0.0"
)

def get_task_service():
    repository = TaskRepository("data/tasks.json")
    return TaskService(repository)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks(
    filters: TaskFilter = Depends(),
    service: TaskService = Depends(get_task_service)
):
    tasks = service.list_tasks(
        status=filters.status,
        priority=filters.priority,
        deadline=filters.deadline,
        before=filters.before,
        after=filters.after
    )
    return [TaskResponse.from_domain(task) for task in tasks]