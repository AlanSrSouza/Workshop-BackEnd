tarefas = []

while True:
    opcao = int(input("DIGITE O QUE FAZER: \n1. Adicionar tarefa \n2. Executar fila de tarefas \n3. Sair:\n "))
    
    if opcao == 1:
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso.")
    elif opcao == 2:
        if tarefas:
            print("Executando fila de tarefas:")
            tarefa_executada = tarefas.pop(0)
            print(f"Sua tarefa: {tarefa_executada}")
        else:
            print("A fila de tarefas está vazia.")
    elif opcao == 3:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")