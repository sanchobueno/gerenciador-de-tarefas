import json
import os
from models.task import Task

class TaskRepository:
    def __init__(self, filepath='data/tasks.json'):
        self.filepath = filepath
        self.tasks = []
        self._load()

#-----------------------------
# Carregar JSON -> memória
#----------------------------- 

    def _load(self):
        if not os.path.exists(self.filepath):
            self._ensure_data_folder()
            self._save()  # Cria o arquivo vazio se não existir
            return
        
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]

                #atualizar o contador de IDs com base no maior ID existente
                if self.tasks:
                    max_id = max(task.id for task in self.tasks)
                    Task._id_counter = max_id + 1
        except Exception:
            self.tasks = []
            self.save()

#-----------------------------
# Salvar memória -> JSON   
#----------------------------- 

    def _save(self):
        data = [task.to_dict() for task in self.tasks]
        self._ensure_data_folder()
       
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    def _ensure_data_folder(self):
        folder = os.path.dirname(self.filepath)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)


#-----------------------------
# Operações CRUD
#-----------------------------

    def add_task(self, task):
        self.tasks.append(task)
        self._save()
        