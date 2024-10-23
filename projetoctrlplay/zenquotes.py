class QuoteElement:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    def __str__(self):
        return self.quote + ' - ' + self.author

import requests

requisicao_raw = requests.get('https://zenquotes.io/api/quotes')
requisicao = requisicao_raw.json()


quotes = []

for i in range(0,49):
    quotes.append(QuoteElement(requisicao[i]['q'], requisicao[i]['a']))

for quote in quotes:
    print(quote)

quoteOne = QuoteElement(requisicao[0]['q'], requisicao[0]['a'])

print(quoteOne)
