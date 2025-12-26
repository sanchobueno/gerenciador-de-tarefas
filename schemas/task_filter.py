from pydantic import BaseModel
from datetime import date
from typing import Optional

class TaskFilter(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    deadline: Optional[date] = None
    before: Optional[date] = None
    after: Optional[date] = None