''' 
OPERADORES UTEIS:
    união '|' união (union) --> Faz a união
    intersecção '&' (intersection) --> Itens presentes em ambos
    diferença '-' --> Itens presentes apenas no set da esquerda
    diferença simétrica '^' --> itens que não estão em ambos
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}

my_set1 = s1 | s2
my_set2 = s1 & s2
my_set3 = s1 - s2
my_set4 = s2 - s1
my_set5 = s1 ^ s2

print(f'{my_set1} --> union')
print(f'{my_set2} --> intersection')
print(f'{my_set3} --> diferença (item da esquerda)')
print(f'{my_set4} --> diferença (item da esquerda)')
print(f'{my_set5} --> diferença simétrica')

