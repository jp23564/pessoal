import json

lista_roupas = []

class Roupa():
    def __init__(self, id_roupa, tipo, tamanho, colecao, cor, marca, material, preco_por_dia):
       self.id_roupa = id_roupa
       self.tipo = tipo
       self.tamanho = tamanho
       self.colecao = colecao
       self.cor = cor
       self.marca = marca
       self.material = material
       self.preco_por_dia = preco_por_dia
    
    def roupa_info(self):
        return self.id_roupa, self.tipo, self.tamanho, self.colecao, self.cor, self.marca, self.material, self.preco_por_dia


    @staticmethod
    def listar_roupas():
        for roupa in lista_roupas:
            print(roupa.roupa_info())
    
    @classmethod
    def criar_roupa(cls):
        id_roupa = input('Insira o ID da peça: ')
        tipo = input('Insira o tipo da peça: ')
        tamanho = input('Insira o tamanho da peça: ')
        colecao = input('Insira a coleção da peça: ')
        cor = input('Insira a cor da peça: ')
        marca = input('Insira a marca da peça: ')
        material = input('Insira o material da peça: ')
        preco_por_dia = input('Insira o preço por dia da peça: ')
        
        nova_roupa = cls(id_roupa, tipo, tamanho, colecao, cor, marca, material, preco_por_dia)
        lista_roupas.append(nova_roupa)

    def alterar_roupa(self):
        print('Você pode alterar:\nID da peça\nTipo da peça\nTamanho da peça\nColeção da peça\nCor da peça\nMarca da peça\nMaterial da peça\nPreço por dia da peça')
        alterar = input('O que deseja alterar sobre a peça?: ')
        if alterar.lower() == 'id':
            self.id_roupa = input('Insira o novo ID da peça: ')
            print('O novo ID da peça é: '+self.id_roupa)
        
        elif alterar.lower() == 'tipo':
            self.tipo = input('Insira o novo tipo da peça: ')
            print('O novo tipo da peça é: '+self.tipo)
        
        elif alterar.lower() == 'tamanho':
            self.tamanho = input('Insira o novo tamanho da peça: ')
            print('O novo tamanho da peça é: '+self.tamanho)
        
        elif alterar.lower() == 'coleção':
            self.colecao = input('Insira a nova coleção da peça: ')
            print('A nova coleção da peça é: '+self.colecao)
        
        elif alterar.lower() == 'cor':
            self.cor = input('Insira a nova cor da peça: ')
            print('A nova cor da peça é: '+self.cor)
        
        elif alterar.lower() == 'marca':
            self.marca = input('Insira a nova marca da peça: ')
            print('A nova marca da peça é: '+self.marca)
        
        elif alterar.lower() == 'material':
            self.material = input('Insira o novo material da peça: ')
            print('O novo material da peça é: '+self.material) 

        elif alterar.lower() == 'preço por dia':
            self.preco_por_dia = input('Insira o novo preço por dia da peça:')
            print('O novo preço por dia da peça é: '+self.preco_por_dia)

    @classmethod
    def remover_roupa(cls):
        roupa_remover = input('Insira o ID da peça que deseja remover: ')
        roupa_encontrada = None

        for roupa in lista_roupas:
            if roupa.id_roupa == roupa_remover:
                roupa_encontrada = roupa
                break
        
        if roupa_encontrada:
            lista_roupas.remove(roupa_encontrada)
            print("Peça removida com sucesso.")
        
        else:
            print("Essa peça não está na lista!")

    def salvar_lista():
        with open('lista_roupas.txt', 'w') as file:
            file.write(json.dumps(lista_roupas))
            print("Lista salva com sucesso.")
    
    def carregar_roupas():
        with open("lista_roupas.txt", 'r') as file:
            print(file.read())

Roupa.criar_roupa()
Roupa.remover_roupa()
Roupa.listar_roupas()