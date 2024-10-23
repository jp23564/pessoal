class Weather():
    def __init__(self, temperatura, velocidade_vento, cidade, temperatura_amanha_max, temperatura_amanha_min):
        self.temperatura = temperatura
        self.velocidade_vento = velocidade_vento
        self.cidade = cidade
        self.temperatura_amanha_max = temperatura_amanha_max
        self.temperatura_amanha_min = temperatura_amanha_min

    def __str__(self):
        return (f'A temperatura atual é: {self.temperatura}\n'
        f'A velocidade do vento é: {self.velocidade_vento}\n'
        f'Você está em: {self.cidade}\n'
        f'A temperatura máxima amanhã será: {self.temperatura_amanha_max}, mínima {self.temperatura_amanha_min}')


import requests

weatherRequestRaw = requests.get('https://api.hgbrasil.com/weather?key=ff3c65ac')

weatherRequest = weatherRequestRaw.json()

weatherOne = Weather(
    weatherRequest['results']['temp'], # temperatura
    weatherRequest['results']['wind_speedy'], # velocidade do vento
    weatherRequest['results']['city'], # cidade
    weatherRequest['results']['forecast'][0]['max'], # previsão de temperatura máxima
    weatherRequest['results']['forecast'][0]['min']) # previsão de temperatura mínima

print(weatherOne)