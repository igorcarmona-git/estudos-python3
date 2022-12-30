#Operadores in e not in

# in -> Se está entre
# not in -> Se não está entre

#Strings são iteráveis

#   0  1  2  3  4  5
#   O  t  á  v  i  o
#  -6 -5 -4 -3 -2 -1

nome = "Otávio"
print(nome[2])
print(nome[-4])

print('á' in nome) #True
print('vio' in nome) #True
print('z' in nome) #False

print(50 * '-')

print('á' not in nome) #False
print('vio' not in nome) #False
print('z' not in nome) #True

print(50 * '-')
print("Exemplo")

nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")

print(50 * '-')

nome = 'Maria Carmo'
 
if ' ' in nome:
    print(f'O nome {nome} tem espaços.')
else:
    print(f'O nome {nome} NÃO tem espaços.')