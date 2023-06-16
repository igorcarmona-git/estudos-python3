"""
EXERCICIOS COM FUNÇÕES!

1- Crie uma função que multiplica todos os argumentos não nomeados recebidos e retorne o total para uma variável e mostre o valor
    da variável. 

2 - Crie uma função que fala se um número é par ou ímpar e retorne se o número é par ou ímpar. 
"""

def product(*args):
    total = 1
    for num in args:
        total *= num
    
    return total

def isPair(num):
    isPAIR = ''
    if (num % 2) == 0: 
        isPAIR = f"The number {num} is PAIR!"
        return isPAIR 
    
    return f"The number {num} is UNPAIRED!"
    
print(f"The product of the numbers is: {product(2, 2, 2, 2)}")
print(isPair(4))
    
# Tente escrever com mais frequência os códigos em inglês, porque pode haver ocasioes que voce vai querer mandar 
# seu código para um servidor e ele não entender, bugar. 