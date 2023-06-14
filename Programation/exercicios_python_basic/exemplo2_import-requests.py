import requests

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json() #Transforma em dicionário para ser lido pelo python
print(cotacoes)
print("\n\n")

cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_real = cotacoes['BTCBRL']['bid']
print(f"DOLAR: {cotacao_dolar} | BRL: {cotacao_real}")

