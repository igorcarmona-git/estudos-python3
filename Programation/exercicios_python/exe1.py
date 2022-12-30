"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n1 = input("Digite um número inteiro: ")

int_n1 = None
valor = None

if n1.isdigit():
    int_n1 = int(n1)
    valor = int_n1 

if valor is None:
    print(f"Você não digitou um número inteiro!")
    exit()

if valor % 2 == 0:
    print(f"O número: {int_n1} é PAR!")
else:
    print(f"O número: {int_n1} é IMPAR!")

###############################################################################################################
# Esse outro jeito aceita números negativos!
# ------------------> Solução melhor <-----------------

num = input('Digite um número ínteiro para saber se é par ou ímpar: ')

try:
    num = int(num)
    if num % 2 == 0:
        print(f'{num} é um número par')
    else:
        print(f'{num} é um número ímpar')
except:
    print('Você não digitou um número inteiro')
