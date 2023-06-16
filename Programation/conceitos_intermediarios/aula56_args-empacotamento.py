""" 
args - ARGUMENTOS NÃO NOMEADOS (Importante serem não nomeados)

* - *args (Empacotamento e Desempacotamento)
"""

#Lmebre-se de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

print("\n\n")

#Exemplo
def soma(*args):   # --> escreve '*args' por convenção entre programadores
    total = 0
    for num in args:
        total += num

    return total

soma1 = soma(2,2)
numeros = 1, 4, 6, 9 #tuple
soma2 = soma(0,10,20,30,40,50) # --> voce consegue passar varios argumentos para os parametros da função
soma3 = sum((1,2,3,4,6,10,30)) # --> função já pronta de um somatório, deve passar iteráveis

print(soma1)
print(soma(*numeros)) # --> função recebe argumentos, voce deve desempacotar para sair da tuple
print(soma2)
print(soma3)