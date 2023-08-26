''' 
Sets são eficientes para remover valores duplicados de iteráveis.
    - Seus valores serão sempre únicos
    - Não aceitam valores mutáveis, ex: list, dict
    - não tem indexes
    - não garantem a ordem
    - são iteráveis (for, in, not in)
'''

#Example:
s1 = {1, 2, 3, 3, 3, 3, 3, 1} 
print(s1)

print('\n\n')

#Você consegue utilizar o set para destinguir valores repetidos de uma lista. Por exemplo, transformar em um 'set' e logo depois transformar para list novamente, voce terá uma lista sem repetição. 

lista = [1, 2, 3, 3, 3, 3, 3, 1]
s2 = set(lista)
lista2 = list(s2)
print(lista2)

#OBS:. Pode-se imaginar o 'set' como uma sacola, e tudo que voce jogar nela só terá itens únicos, fora de ordem. 

#OBS-2:. 'True e 1' são considerados valores iguais, assim como '0 e False':
print('\n\n')

my_set = {"apple", "banana", "cherry", True, 1, 2, 0, False}
print(my_set)