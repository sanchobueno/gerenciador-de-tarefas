from models import task
from models.task import Task

class TaskService:
    def __init__(self, repository):
        self.repository = repository


        #-----------------------------
        # Cria tarefa
        #-----------------------------

    def create_task(self, titulo, descricao="", prioridade="Média", deadline=None):
            if not titulo or not titulo.strip():
                raise ValueError("O título da tarefa não pode ser vazio.")
            
            task = Task(
                titulo=titulo.strip(),
                descricao=descricao.strip(),
                prioridade=prioridade,
                deadline=deadline
            )
            return self.repository.add(task)
        
        #-----------------------------
        # Lista todas as tarefas
        #-----------------------------

    def list_tasks(self):
            return self.repository.get_all()
        
        #-----------------------------
        # concluir tarefa
        #-----------------------------

    def complete_task(self, task_id):
            task = self.repository.get_by_id(task_id)

            if not task:
                raise ValueError("Tarefa não encontrada.")

            if task.status == "concluida":
                raise ValueError("A tarefa já está concluída.")

            task.status = "concluida"
            self.repository.update(task)
            return task

            
    
        
        #-----------------------------
        # atualizar tarefa
        #-----------------------------

    def update_task(self, task_id, titulo=None, descricao=None, prioridade=None, deadline=None):
            task = self.repository.get_by_id(task_id)
            
            if not task:
                raise ValueError("Tarefa não encontrada.")
            if titulo is not None:
                if not titulo.strip():
                    raise ValueError("O título da tarefa não pode ser vazio.")
                task.titulo = titulo.strip()

            if descricao is not None:
                task.descricao = descricao.strip()
            
            if prioridade is not None:
                task.prioridade = task._validate_priority(prioridade)

            if deadline is not None:
                task.deadline = task._validate_deadline(deadline)
            
            self.repository.update(task)
            return task
        
        #-----------------------------
        # deletar tarefa
        #-----------------------------

    def delete_task(self, task_id):
            if not self.repository.delete(task_id):
                raise ValueError("Tarefa não encontrada.")
            return True