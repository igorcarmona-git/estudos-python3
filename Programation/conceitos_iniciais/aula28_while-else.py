"""
É um recurso específico de Python, mas não é muito utilizado.
while/else
"""

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.') #Geralmente usado para quando há alguma condição dentro do while e você quer printar algo. 
print('Fora do while.')

# Sempre que encontramos o break no laço de repetição o 'else' não é executado. 
# Quando o laço vai até o final, o 'else' é executado. 