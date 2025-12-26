from fastapi import FastAPI
from repositories.task_repository import TaskRepository
from services.task_service import TaskService
from typing import Optional


repository = TaskRepository()
service = TaskService(repository)


app = FastAPI(
    title="Gerenciador de Tarefas API",
    description="API para gerenciar tarefas, permitindo criar, ler, atualizar e deletar tarefas.",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/tasks")
def list_tasks(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    deadline: Optional[str] = None,
    before: Optional[str] = None,
    after: Optional[str] = None
):
    tasks = service.list_tasks(
        status=status,
        priority=priority,
        deadline=deadline,
        before=before,
        after=after
    )
    return tasks