import json
from cliente import Cliente
from roupa import Roupa
from locacao import Locacao

def menu():
    try:
        menu_alterar = int(input("O que deseja alterar?\n[1] Roupas\n[2] Locações\n[3] Clientes "))

        if menu_alterar == 1:
            Roupa.menu_roupas()
        
        if menu_alterar == 2:
            Locacao.menu_locacoes()

        if menu_alterar == 3:
            Cliente.menu_clientes()

        elif menu_alterar not in [1,2,3]:
            print("Escolha um número de 1-3.")
            menu()

    except:
        print("Houve um erro, tente novamente.")
        menu()

menu()

