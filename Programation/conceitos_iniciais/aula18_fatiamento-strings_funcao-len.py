"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] --> [inicio : fim : pula-quantos em quantos]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
print(variavel[4:8])
print(variavel[4:]) # vai de 'm' até o final da string
print(variavel[:4]) # vai desde o começo da string até 'á'

# OBS: O índice final geralmente não é incluído, exemplo:
# print(variavel[4:8]) --> Vai imprimir de 'm' até 'd', mesmo que o [8] seja 'o' 

print(len(variavel))

# A função len() retorna o tamanho da string

print(variavel[0:len(variavel):4]) # printa a string pulando de 4 em 4
print(variavel[::-1]) # printa a string invertida, pega do ínicio : fim ao contrário 