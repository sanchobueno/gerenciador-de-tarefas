# 📝 Gerenciador de Tarefas (CLI em Python)

Projeto desenvolvido em **Python** com foco em aprendizado prático de programação, aplicando **boas práticas**, **arquitetura em camadas** e **testes automatizados**.

O sistema permite gerenciar tarefas via terminal (CLI), com persistência em arquivo JSON, validação de dados e testes que garantem a estabilidade da aplicação.

---

## 🎯 Objetivo do Projeto

Este projeto foi criado com fins de **estudo e portfólio**, com os seguintes objetivos:

- Consolidar fundamentos de Python
- Aplicar Programação Orientada a Objetos
- Entender separação de responsabilidades
- Implementar um CRUD completo
- Aprender testes automatizados com `pytest`
- Trabalhar com arquivos e sistema de arquivos
- Criar uma base sólida para futuras evoluções (API, banco de dados, etc.)

---

## ⚙️ Funcionalidades

- Criar tarefas
- Listar tarefas
- Marcar tarefas como concluídas
- Excluir tarefas
- Persistência de dados em arquivo JSON
- Validação de entradas do usuário
- Normalização de texto (acentos, espaços e maiúsculas/minúsculas)
- Testes automatizados cobrindo as principais regras de negócio

---

## 🧱 Arquitetura do Projeto

O projeto foi estruturado com **camadas bem definidas**, simulando um projeto real de mercado:

projeto_gerenciador/
│
├── main.py # Interface CLI (entrada do usuário)
│
├── models/ # Regras de domínio
│ ├── init.py
│ └── task.py
│
├── repositories/ # Persistência de dados (JSON)
│ ├── init.py
│ └── task_repository.py
│
├── services/ # Regras de negócio
│ ├── init.py
│ └── task_service.py
│
├── tests/ # Testes automatizados
│ ├── init.py
│ ├── test_task_model.py
│ ├── test_task_repository.py
│ └── test_task_service.py
│
└── data/
└── tasks.json


---

## 📌 Responsabilidade de Cada Camada

- **Model (`models`)**  
  Responsável por:
  - Estrutura da entidade `Task`
  - Validação dos dados
  - Normalização de texto
  - Regras básicas do domínio

- **Repository (`repositories`)**  
  Responsável por:
  - Operações de CRUD
  - Leitura e escrita no arquivo JSON
  - Isolamento da persistência

- **Service (`services`)**  
  Responsável por:
  - Regras de negócio
  - Orquestração entre Model e Repository
  - Validações de alto nível

- **CLI (`main.py`)**  
  Responsável por:
  - Interação com o usuário
  - Entrada e saída de dados no terminal

- **Tests (`tests`)**  
  Responsável por:
  - Garantir que tudo funcione corretamente
  - Validar regras de negócio
  - Evitar regressões futuras

---

## 🧠 Conceitos Aplicados

- Programação Orientada a Objetos (OOP)
- Arquitetura em camadas
- CRUD (Create, Read, Update, Delete)
- Validação e sanitização de dados
- Normalização de strings com `unicodedata`
- Testes unitários com `pytest`
- Isolamento de dependências
- Uso de diretórios temporários em testes (`tempfile`)
- Boas práticas de organização de código

---

## 🧪 Testes Automatizados

O projeto possui **testes automatizados** cobrindo as principais funcionalidades.

### Executar os testes:

"```bash
pytest -v"

### Exemplo de resultado esperado:
collected 9 items
9 passed in 0.14s

## Cobertura dos testes:

Criação de tarefas válidas

Validação de prioridades inválidas

Validação de datas inválidas

Normalização de prioridade (acentos e letras)

Operações de CRUD no repositório

Regras de negócio do service

## 🚀 Como Executar o Projeto
1️⃣ Clonar o repositório
git clone <url-do-repositorio>

2️⃣ Acessar a pasta do projeto
cd projeto_gerenciador

3️⃣ Executar a aplicação
python main.py

## 📦 Dependências

Python 3.10+

pytest (para testes)

Instalar o pytest:

pip install pytest

## 🔮 Próximas Evoluções Planejadas

Substituir entradas via input() por argparse

Migrar persistência de JSON para SQLite

Criar uma API REST usando FastAPI

Aumentar cobertura e qualidade dos testes

Criar uma interface web ou frontend

## 👤 Autor

Lucas Bueno

Projeto desenvolvido com foco em aprendizado prático e construção de portfólio em Python.