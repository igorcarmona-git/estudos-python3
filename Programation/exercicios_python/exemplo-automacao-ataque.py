# O replit é uma forma de Cloud Computing
# Exemplo de automação de ataque a alvos usando python

# dict / dicionário (Objetos) --> Possuem 'chave': valor

teste = {
  'dominio': "terra.com.br", 
  'sistema': "Linux",
  'portas': [10, 20, 30]
}

teste2 = {
  'dominio': "google.com.br", 
  'sistema': "Mac",
  'portas': [34, 24, 302]
}

teste3 = {
  'dominio': "globo.com.br", 
  'sistema': "windows",
  'portas': [1440, 2033, 3045]
}

# LISTAS com dict dentro
alvos = [teste, teste2, teste3] 

# print(alvos[1])

for alvo in alvos:
  print("Atacando --> ", alvo["dominio"])
  print("Atacando com o ataque para", alvo["sistema"])
  print()

###################################################################################################################################

# O primeiro loop for itera em cada sublista de salas e atribui as variáveis nomes e valores aos respectivos elementos da sublista. Em seguida, é impressa a lista de nomes. Depois, o segundo loop for itera em cada elemento da lista valores e imprime o valor correspondente. Note que a variável nomes contém uma tupla com os nomes das pessoas da sala, enquanto a variável valores contém uma lista de valores associados a essa sala.

salas = [[['Maria', 'Helena'], [0, 10, 20]], [['Elaine'], [30, 40]]]
 
for nomes, valores in salas:
    print(nomes)
    for valor in valores:
        print(valor)