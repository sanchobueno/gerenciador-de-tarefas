from pydantic import BaseModel
from datetime import date
from typing import Optional
from models.task import Task

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    status: str
    deadline: Optional[date]

    @classmethod
    def from_domain(cls, task: Task) -> "TaskResponse":
        return cls(
            id=task.id,
            title=task.titulo,
            description=task.descricao,
            priority=task.prioridade,
            status=task.status,
            deadline=task.deadline
        )   