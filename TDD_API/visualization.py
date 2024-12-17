import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_parquet("./gold/stocks_gold.parquet")

plt.figure(figsize=(10, 6))

for symbol in df['symbol'].unique():
    symbol_data = df[df['symbol'] == symbol]
    plt.plot(symbol_data['date'], symbol_data['preco'], label=symbol)

plt.title('Preço das Ações ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço')


plt.legend(title='Symbol')

plt.savefig('stocks_prices.png')