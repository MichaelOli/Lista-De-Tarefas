# Lista para armazenar as tarefas
tarefas = []

# Loop para adicionar tarefas
while True:
    # Solicita o nome da tarefa
    print(f'{'='*20} Adicionando tarefas {'='*20}')
    add_tarefa = input('Informe o nome de uma tarefa ou aperte "enter" para exibir a lista: ')

    # Verifica se o usuário inseriu uma tarefa ou deseja exibir a lista
    if add_tarefa:
        tarefas.append(add_tarefa)
    else:
        break

# Exibe a lista de tarefas
for tarefa in tarefas:
    print(tarefa)
