"""
.appned() --> Adiciona um item ao final da list
.insert(posição, valor) --> Adiciona um item no índice escolhido
.pop() --> Remove o último item da list
.del() --> Deleta um índice
.clear() --> Limpa a lista
.extend() --> Estende a lista
+ - --> Concatena listas

"""

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz') #Python acusa erro, mas pode ser feito. 
lista.append(1233)
del lista[-1] # --> -1 sempre é o último índice
# lista.clear()
lista.insert(100, 5)
print(lista)
print(lista[5])

# OBS --> Por mais que você coloque o '5' na posição 100, ele leva em consideração que é o ultimo item, pois não tem 100 posições na list
# na verdade, ele está na posição 5.