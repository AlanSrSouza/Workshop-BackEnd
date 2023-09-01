tarefas = []

while True:
    opcao = int(input(
        "DIGITE O QUE FAZER: \n1. Adicionar tarefa \n2. Executar última tarefa \n3. Sair:\n "))

    if opcao == 1:
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso.")
    elif opcao == 2:
        if tarefas:
            print("Executando última tarefa:")
            tarefa_executada = tarefas.pop()
            print(f"Sua tarefa: {tarefa_executada}")
        else:
            print("A pilha de tarefas está vazia.")
    elif opcao == 3:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
