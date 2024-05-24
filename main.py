#Variavel que recebe a lista

tarefas =[]
    
# nova tarefa é inserida na lista
while True:
# usuario informa o nome da nova fruta
    add_tarefa = input('Informe o nome de uma tarefa ou simplesmente aperte "enter" para que a lista seja exibida:  ')
#Verifica se o usuario inseriu a nova tarefa
    if add_tarefa !='':
        tarefas.append(add_tarefa)
        continue
    else:
        break
# exibe na tela a nova lista
for tarefa in tarefas:        
    print(tarefa)

