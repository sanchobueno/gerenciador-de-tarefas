from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Título da tarefa")
    description: Optional[str] = Field(None, description="Descrição da tarefa")
    priority: Optional[str] = Field(default="media", description="Prioridade da tarefa: baixa, media, alta")
    deadline: Optional[date] = Field(None, description="Data limite para a tarefa no formato AAAA-MM-DD")

