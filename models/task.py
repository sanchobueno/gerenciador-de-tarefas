import datetime

class Task:
    VALID_PRIORITIES = ['Baixa', 'Média', 'Alta']
    VALID_STATUS = ['Pendente', 'Em Progresso', 'Concluída']
    _id_counter = 1

    def __init__(self, titulo, descricao="", prioridade="Média", deadline=None, status='Pendente', task_id=None):
        self.id = task_id if task_id is not None else Task._generate_id()
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = self._validate_priority(prioridade)
        self.status = self._validate_status(status)
        self.deadline = self._validate_deadline(deadline)


#--------------------------------
# validações
#--------------------------------

    def _validate_priority(self, value):
        if value not in Task.VALID_PRIORITIES:
            raise ValueError(f"Prioridade inválida: {value}. Valores válidos são: {self.VALID_PRIORITIES}")
        return value
    
    def _validate_status(self, value):
        if value not in Task.VALID_STATUS:
            raise ValueError(f"Status inválido: {value}. Valores válidos são: {self.VALID_STATUS}")
        return value
    
    def _validate_deadline(self, deadline):
        if deadline is None:
            return None
        if isinstance(deadline, datetime.date):
            return deadline
        try:
            return datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Deadline deve estar no formato 'YYYY-MM-DD' ou ser um objeto datetime.date")
        
#--------------------------------
# conversão para JSON
#--------------------------------

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status,
            "deadline": self.deadline.isoformat() if self.deadline else None,
        }
    
# ----------------------------
# geração automática de ID
# ----------------------------
    @staticmethod
    def _generate_id():
        task_id = Task._id_counter
        Task._id_counter += 1
        return task_id
    
# ----------------------------
# fábrica a partir de dicionário
# ----------------------------

    @staticmethod
    def from_dict(data):
        return Task(
            titulo=data["titulo"],
            descricao=data.get("descricao"),
            prioridade=data.get("prioridade", "Média"),
            deadline=data.get("deadline"),
            status=data.get("status", "Pendente"),
            task_id=data.get("id")
        )
    