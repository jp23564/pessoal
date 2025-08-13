import pandas as pd

data = {
    'Nome': ['Luiz', 'Gabriel', 'João', 'Paulo'],
    'Idade': ['16', '15', '19', '24'],
    'Cidade': ['Jundiaí', 'São Paulo', 'Francisco Morato', 'Campinas']
}

cadastro = pd.DataFrame(data)
print(cadastro)