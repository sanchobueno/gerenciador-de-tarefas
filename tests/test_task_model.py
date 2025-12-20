import pytest
from models.task import Task

def test_create_task_with_valid_data():
    task = Task(
        titulo="Estudar python",
        descricao="aprender testes",
        prioridade="alta",
        deadline="2024-12-31"
    )

    assert task.titulo == "Estudar python"
    assert task.descricao == "aprender testes"
    assert task.prioridade == "alta"
    assert task.deadline.isoformat() == "2024-12-31"

def test_invalid_priority_raises_error():
    with pytest.raises(ValueError):
        Task(titulo="Teste", prioridade="urgente")


def test_invalid_deadline_raises_error():
    with pytest.raises(ValueError):
        Task(titulo="Teste", deadline="31-12-2024")

def test_priority_accepts_accents_and_case():
    task = Task(titulo="Teste", prioridade="ÁLTA")
    assert task.prioridade == "alta"

    task = Task(titulo="Teste", prioridade=" Média ")
    assert task.prioridade == "media"