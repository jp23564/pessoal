import json

lista_locacoes = []

class Locacao():
    def __init__(self, id_emprestimo, cpf_cliente, id_produto, data_locacao, data_devolucao, valor_a_pagar, estado_locacao):
       self.id_emprestimo = id_emprestimo
       self.cpf_cliente = cpf_cliente
       self.id_produto = id_produto
       self.data_locacao = data_locacao
       self.data_devolucao = data_devolucao
       self.valor_a_pagar = valor_a_pagar
       self.estado_locacao = estado_locacao


    
    def locacao_info(self):
        return self.id_emprestimo, self.cpf_cliente, self.id_produto, self.data_locacao, self.data_devolucao, self.valor_a_pagar, self.estado_locacao
    
    @staticmethod
    def listar_locacoes():
        for locacao in lista_locacoes:
            print(locacao.locacao_info())
    
    @classmethod
    def criar_locacao(cls):
        id_emprestimo = input('Insira o ID do empréstimo: ')
        cpf_cliente = input('Insira o CPF do cliente: ')
        id_produto = input('Insira o ID do produto: ')
        data_locacao = input('Insira a data da locação: ')
        data_devolucao = input('Insira a data de devolução: ')
        valor_a_pagar = input('Insira o valor a pagar por dia: ')
        estado_locacao = input('Insira o estado atual da locação: ')

        nova_locacao = cls(id_emprestimo, cpf_cliente, id_produto, data_locacao, data_devolucao, valor_a_pagar, estado_locacao)
        lista_locacoes.append(nova_locacao)

    def alterar_locacao(self):
        print('Você pode alterar:\nID do empréstimo\nCPF do cliente\nID do produto\nData da locação\nData de devolução\nValor a pagar\nEstado da locação')
        alterar = input('O que deseja alterar sobre a peça?: ')
        if alterar.lower() == 'id':
            alterar = input('Qual ID deseja alterar, empréstimo ou produto?: ')
            if alterar.lower() == 'empréstimo':
                self.id_emprestimo = input('Insira o novo ID do empréstimo: ')
                print('O novo ID do empréstimo é: '+self.id_emprestimo)
            elif alterar.lower() == 'produto':
                self.id_produto = input('Insira o novo ID do produto: ')
                print('O novo ID do produto é: '+self.id_produto)
        
        elif alterar.lower() == 'cpf':
            self.tipo = input('Insira o novo CPF do cliente: ')
            print('O novo CPF do cliente é: '+self.cpf_cliente)
        
        elif alterar.lower() == 'data':
            alterar = input('Qual data deseja alterar, locação ou devolução?: ')
            if alterar.lower() == 'locação':
                self.id_emprestimo = input('Insira a nova data de locação: ')
                print('A nova data de locação é: '+self.data_locacao)
            elif alterar.lower() == 'devolução':
                self.data_devolucao = input('Insira a nova data de devolução: ')
                print('A nova data de devolução é: '+self.data_devolucao)
        
        elif alterar.lower() == 'valor a pagar':
            self.valor_a_pagar = input('Insira o novo valor a pagar: ')
            print('O novo valor a pagar é: '+self.valor_a_pagar)
        
        elif alterar.lower() == 'estado da locação':
            self.estado_locacao = input('Insira o novo estado da locação: ')
            print('O novo estado da locação é: '+self.estado_locacao)

    @classmethod
    def remover_locacao(cls):
        locacao_remover = input('Insira o ID da locação que deseja remover: ')
        locacao_encontrada = None

        for locacao in lista_locacoes:
            if locacao.id_emprestimo == locacao_remover:
                locacao_encontrada = locacao
                break
        
        if locacao_encontrada:
            lista_locacoes.remove(locacao_encontrada)
            print("Locação removida com sucesso.")
        
        else:
            print("Essa locação não está na lista!")

    def salvar_lista():
        with open('lista_locacoes.txt', 'w') as file:
            file.write(json.dumps(lista_locacoes))
            print("Lista salva com sucesso.")
    
    def carregar_locacoes():
        with open("lista_locacoes.txt", 'r') as file:
            print(file.read())
