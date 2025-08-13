import json

lista_clientes = []

class Cliente():
    try:
        def __init__(self, nome, cpf, data_nascimento, endereco, email, telefone, data_registro):
            self.nome = nome
            self.cpf = cpf
            self.data_nascimento = data_nascimento
            self.endereco = endereco
            self.email = email
            self.telefone = telefone
            self.data_registro = data_registro

        def cliente_info(self):
            return self.nome, self.cpf, self.data_nascimento, self.endereco, self.email, self.telefone, self.data_registro

        @staticmethod
        def listar_clientes():
            for cliente in lista_clientes:
                print(cliente.cliente_info())
            if lista_clientes == []:
                print('A lista está vazia.')
        
        @classmethod
        def criar_cliente(cls):
            cpf = input('Insira o CPF do cliente: ')

            for cliente in lista_clientes:
                if cliente.cpf == cpf:
                    print("Esse CPF já está cadastrado!")
                    return
            
            nome = input('Insira o nome do cliente: ')
            data_nascimento = input('Insira a data de nascimento do cliente: ')
            endereco = input('Insira o endereço do cliente: ')
            email = input('Insira o e-mail do cliente: ')
            telefone = input('Insira o telefone do cliente: ')
            data_registro = input('Insira a data de registro do cliente: ')
            
            novo_cliente = cls(nome, cpf, data_nascimento, endereco, email, telefone, data_registro)
            lista_clientes.append(novo_cliente)
                
        @classmethod
        def alterar_cliente(cls):
            cpf_alterar = input('Digite o CPF do cliente que deseja alterar: ')
            
            for cliente in lista_clientes:
                if cliente.cpf == cpf_alterar:
                    print(f'Cliente encontrado: {cliente.nome}')
                    print('Você pode alterar:\nNome\nCPF\nData de nascimento\nEndereço\nE-mail\nTelefone\nData de registro')
                    
                    alterar = input('O que deseja alterar sobre o cliente? ')
                    if alterar.lower() == 'nome':
                        cliente.nome = input('Insira o novo nome do cliente: ')
                        print('O novo nome do cliente é: '+cliente.nome)
                    
                    elif alterar.lower() == 'cpf':
                        cliente.cpf = input('Insira o novo CPF do cliente: ')
                        print('O novo CPF do cliente é: '+cliente.cpf)
                    
                    elif alterar.lower() == 'data de nascimento':
                        cliente.data_nascimento = input('Insira a nova data de nascimento do cliente: ')
                        print('A nova data de nascimento do cliente é: '+cliente.data_nascimento)
                    
                    elif alterar.lower() == 'endereço':
                        cliente.endereco = input('Insira o novo endereço do cliente: ')
                        print('O novo endereço do cliente é: '+cliente.endereco)
                    
                    elif alterar.lower() in ['email', 'e-mail']:
                        cliente.email = input('Insira o novo e-mail do cliente: ')
                        print('O novo e-mail do cliente é: '+cliente.email)
                    
                    elif alterar.lower() == 'telefone':
                        cliente.telefone = input('Insira o novo telefone do cliente: ')
                        print('O novo telefone do cliente é: '+cliente.telefone)
                    
                    elif alterar.lower() == 'data de registro':
                        cliente.data_registro = input('Insira a nova data de registro do cliente: ')
                        print('A nova data de registro do cliente é: '+cliente.data_registro)  
            
        @classmethod
        def remover_cliente(cls):
            cpf_remover = input('Insira o CPF do cliente que deseja remover: ')
            cliente_encontrado = None

            for cliente in lista_clientes:
                if cliente.cpf == cpf_remover:
                    cliente_encontrado = cliente
                    break
            
            if cliente_encontrado:
                lista_clientes.remove(cliente_encontrado)
                print("Cliente removido com sucesso.")

            else:
                print("Esse cliente não está na lista!")

        def salvar_lista():
            with open('lista_clientes.txt', 'w') as file:
                file.write(json.dumps(lista_clientes))
                print("Lista salva com sucesso.")
        
        def carregar_clientes():
            with open("lista_clientes.txt", 'r') as file:
                print(file.read())

        @classmethod
        def menu_clientes(cls):
            escolha = input("O que deseja fazer?\n[1] Listar clientes\n[2] Criar cliente\n[3] Alterar cliente\n[4] Remover cliente\n[5] Salvar lista de clientes\n[6] Carregar lista de clientes\n")

            if escolha == '1':
                Cliente.listar_clientes()
                Cliente.menu_clientes()

            elif escolha == '2':
                Cliente.criar_cliente()
                Cliente.menu_clientes()

            elif escolha == '3':
                Cliente.alterar_cliente()
                Cliente.menu_clientes()
            
            elif escolha == '4':
                Cliente.remover_cliente()
                Cliente.menu_clientes()

            elif escolha == '5':
                Cliente.salvar_lista()
                Cliente.menu_clientes()

            elif escolha == '6':
                Cliente.carregar_clientes()
                Cliente.menu_clientes()

    except:
        print("Houve um erro, tente novamente.")
            
Cliente.listar_clientes()
joao = Cliente('5','8','5','5','5','5','5')
