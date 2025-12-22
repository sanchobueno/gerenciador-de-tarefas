import argparse

from repositories.task_repository import TaskRepository
from services.task_service import TaskService


def main():

    repo = TaskRepository()
    service = TaskService(repo)

    parser = argparse.ArgumentParser(
        description="Gerenciador de Tarefas (CLI)"
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True
        )
    #---------------create

    create_parser = subparsers.add_parser(
        "create",
        help="Criar uma nova tarefa"
    )

    create_parser.add_argument(
        "--title",
        required=True,
        help="Título da tarefa"
    )

    create_parser.add_argument(
        "--description",
        default="",
        help="Descrição da tarefa"
    )

    create_parser.add_argument(
        "--priority",
        default="media",
        choices=["baixa", "media", "alta"],
        help="Prioridade da tarefa(baixa, media, alta)"
    )

    create_parser.add_argument(
        "--deadline",
        default=None,
        help="Deadline da tarefa (YYYY-MM-DD)"
    )

    #---------------list   
    # Subcomando: list
    list_parser = subparsers.add_parser(
        "list",
        help="Listar todas as tarefas"
    )

    list_parser.add_argument(
        "--status",
        choices=["pendente", "em progresso", "concluida"],
        default=None,
        help="Filtrar tarefas por status"
    )

    list_parser.add_argument(
        "--priority",
        choices=["baixa", "media", "alta"],
        default=None,
        help="Filtrar tarefas por prioridade"
    )

    list_parser.add_argument(
        "--deadline",
        help="Filtrar tarefas por deadline (YYYY-MM-DD)"
    )

    list_parser.add_argument(
        "--before",
        help="Listar tarefas com deadline antes da data (YYYY-MM-DD)"
        )

    list_parser.add_argument(
        "--after",
        help="Listar tarefas com deadline depois da data (YYYY-MM-DD)"
        )


    #--------------subcomando: complete

    complete_parser = subparsers.add_parser(
        "complete",
        help="Marcar uma tarefa como concluída"
    )

    complete_parser.add_argument(
        "--id",
        type=int,
        required=True,
        help="ID da tarefa a ser concluída"
    )

    #----------------delete
    # Subcomando: delete
    delete_parser = subparsers.add_parser(
        "delete",
        help="Deletar uma tarefa"
    )

    delete_parser.add_argument(
        "--id",
        type=int,
        required=True,
        help="Deletar uma tarefa"
    )


# Parse os argumentos da linha de comando
    args = parser.parse_args()



#------------execução create-------------
    if args.command == "create":
        try:
            task = service.create_task(
                titulo=args.title,
                descricao=args.description,
                prioridade=args.priority,
                deadline=args.deadline
            )
            print("✅ Tarefa criada com sucesso!")
            print(f"ID: {task.id}")
            print(f"Título: {task.titulo}")
            print(f"Prioridade: {task.prioridade}")
            print(f"Status: {task.status}")
            print(f"Deadline: {task.deadline}")

        except ValueError as e:
            print(f"Erro ao criar tarefa: {e}")



#------------execução list-------------
    elif args.command == "list":
        tasks = service.list_tasks(
            status=args.status,
            priority=args.priority,
            deadline=args.deadline,
            before=args.before,
            after=args.after
        )
        if not tasks:
            print("📭 Nenhuma tarefa cadastrada.")
            return
        print("📋 Lista de tarefas:\n")
        for task in tasks:
            status = "✔" if task.status == "concluida" else " "
            print(
            f"[{status}] "
            f"ID {task.id} | "
            f"{task.titulo} "
            f"(Prioridade: {task.prioridade})"
            f"(deadline: {task.deadline})"
        )
            



#------------execução complete-------------
    elif args.command == "complete":
        try:
            task = service.complete_task(args.id)

            print("✅ Tarefa concluída com sucesso!")
            print(f"ID: {task.id}")
            print(f"Título: {task.titulo}")
            print(f"Status: {task.status}")

        except ValueError as e:
            print(f"❌ Erro: {e}")
#------------execução delete-------------
    elif args.command == "delete":
        try:
            service.delete_task(args.id)
            print("✅ Tarefa deletada com sucesso!")
        except ValueError as e:
            print(f"❌ Erro: {e}")



if __name__ == "__main__":
    main()

