import json

with open('bronze/stocks_bronze.json', "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
print(dados)