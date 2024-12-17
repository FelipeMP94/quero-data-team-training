import json
import pandas as pd




with open('bronze/stocks_bronze.json', "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)


stocks = ["AAPL","AMZN","UNH","TSLA","NVDA","GOOG"," META","INTR","TSM","NFLX "]
dados_total = []
for i in range(len(dados)):
    for j in range(len(dados[i]['data'])):
        dados[i]['data'][j]['symbol'] = stocks[i]
    dados_total = dados_total + dados[i]['data']

print(dados[i]['data'])
table = pd.DataFrame(data = dados_total)
print(table.columns)
print(len(table))                            