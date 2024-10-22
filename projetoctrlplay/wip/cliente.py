import json

lista_clientes = []

class Cliente():
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
    
    @classmethod
    def criar_cliente(cls):
        nome = input('Insira o nome do cliente: ')
        cpf = input('Insira o CPF do cliente: ')
        data_nascimento = input('Insira a data de nascimento do cliente: ')
        endereco = input('Insira o endereço do cliente: ')
        email = input('Insira o e-mail do cliente: ')
        telefone = input('Insira o telefone do cliente: ')
        data_registro = input('Insira a data de registro do cliente: ')
        
        novo_cliente = cls(nome, cpf, data_nascimento, endereco, email, telefone, data_registro)
        lista_clientes.append(novo_cliente)

    def alterar_cliente(self):
        print('Você pode alterar:\nNome\nCPF\nData de nascimento\nEndereço\nE-mail\nTelefone\nData de registro')
        alterar = input('O que deseja alterar sobre o cliente? ')
        if alterar.lower() == 'nome':
            self.nome = input('Insira o novo nome do cliente: ')
            print('O novo nome do cliente é: '+self.nome)
        
        elif alterar.lower() == 'cpf':
            self.cpf = input('Insira o novo CPF do cliente: ')
            print('O novo CPF do cliente é: '+self.cpf)
        
        elif alterar.lower() == 'data de nascimento':
            self.data_nascimento = input('Insira a nova data de nascimento do cliente: ')
            print('A nova data de nascimento do cliente é: '+self.data_nascimento)
        
        elif alterar.lower() == 'endereço':
            self.endereco = input('Insira o novo endereço do cliente: ')
            print('O novo endereço do cliente é: '+self.endereco)
        
        elif alterar.lower() == 'email' or 'e-mail':
            self.email = input('Insira o novo e-mail do cliente: ')
            print('O novo e-mail do cliente é: '+self.email)
        
        elif alterar.lower() == 'telefone':
            self.telefone = input('Insira o novo telefone do cliente: ')
            print('O novo telefone do cliente é: '+self.telefone)
        
        elif alterar.lower() == 'data de registro':
            self.data_registro = input('Insira a nova data de registro do cliente: ')
            print('A nova data de registro do cliente é: '+self.data_registro)  
    
    @classmethod
    def remover_cliente(cls):
        nome_remover = input('Insira o nome do cliente que deseja remover: ')
        cliente_encontrado = None

        for cliente in lista_clientes:
            if cliente.nome == nome_remover:
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
            

Cliente.criar_cliente()
Cliente.criar_cliente()
Cliente.listar_clientes()
Cliente.remover_cliente()
Cliente.listar_clientes()
