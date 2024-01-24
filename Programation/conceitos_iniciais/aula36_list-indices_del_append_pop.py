"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +

Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido -->', ultimo_valor)

"""
OBS:  As vezes o seu programa pode ficar lento por voce ter uma lista muito grande e deletou ou moveu algum item do começo dessa lista. 
      O Python terá o trabalho de reorganizar todos esses itens. 

.append() --> Adiciona um item ao final da list
.insert(posição, valor) --> Adiciona um item no índice escolhido
.pop() --> Remove o último item da list
del --> Deleta um índice
.clear() --> Limpa a lista
.extend() --> Estende a lista
+ - --> Concatena listas

"""