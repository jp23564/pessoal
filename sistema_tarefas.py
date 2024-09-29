
import json 

tarefas = {}

def menu():
    
    while True:
        with open("tarefas.txt", 'r') as file:
            file.read()

        print("Bem vindo(a)! O que deseja fazer?")
        print("\n[1] Adicionar tarefa a lista\n[2] Remover uma tarefa da lista\n[3] Mostrar a lista de todas as tarefas\n[4] Salvar a lista de tarefas\n[5] Carregar a lista de tarefas\n[6] Sair do programa\n")
        escolha = input("Digite um número para fazer a sua escolha: ")
        if escolha == '1':
            adicionar_tarefa()
            
        elif escolha == '2':
            remover_tarefa()
            
        elif escolha == '3':
            listar_tarefas()
            
        elif escolha == '4':
            salvar_tarefas()
            
        elif escolha == '5':
            carregar_tarefas()
            
        elif escolha == '6':
            print("Obrigado por usar o programa!")
            break
        
        else:
            print("Sua escolha precisa ser um número de 1-6!")
            

def adicionar_tarefa():
    titulo = input("Insira um breve título da sua tarefa: ")
    descricao = input("Insira uma descrição breve da sua tarefa: ")
    tarefas[titulo] = descricao 

def remover_tarefa():
    titulo = input("Insira o titulo da tarefa que deseja remover: ")
    if titulo not in tarefas:
        print("Essa tarefa não existe!")
        menu()
    else:
        del tarefas[titulo.lower()]
        print("Tarefa removida com sucesso! Aqui está a lista atual de tarefas:")
        listar_tarefas()
    

def listar_tarefas(): 
    if tarefas == {}:
        print("A lista está vazia!")

    else:
    
        keys = list(tarefas.keys())
        values = list(tarefas.values())

        for index, tarefa in enumerate(tarefas):
            print("Tarefa "+str(index+1)+":", keys[index].capitalize()+";", values[index].capitalize()) 

def salvar_tarefas():
    with open('tarefas.txt', 'w') as file:
        file.write(json.dumps(tarefas))
    print("Lista salva com sucesso.")

def carregar_tarefas():
    with open("tarefas.txt", 'r') as file:
        print(file.read())

menu()

