# Imprecisão de ponto flutuante.   

# Talvez você pode acabar encontrando esse tipo de problema

# A função 'round' arredonda valores tipo float

import decimal

number1 = 0.1
number2 = 0.7

number3 = number1 + number2

print(number3)

print()
####################### Como contornar esse problema #######################

# FORMA 1:
print(f'{number3:.2f}\n') # formata o texto dentro da string, mas retorna um tipo string. 

#FORMA 2:
print(round(number3)) #Arredonda o valor e retorna um tipo float. 
print(round(number3, 2)) # Com duas casas decimas, retorna um tipo float. 
print(round(number3, 10)) # Se as 10 casas decimais for o mesmo numero, não mostra.

# OBS: Para valores decimais muito grandes e você precisa fazer um programa que calcule melimetricamente com muita precisão.
# Pode-se usar 'import decima' e chamar a função 'decimal.Decimal('')'. Deve-se passar uma string, que a função irá fazer o trabalho
# de converter para o float correto. 
print("\n\n\n")

#FORMA 3:
n1 = decimal.Decimal('0.1')
n2 = decimal.Decimal('0.7')
n3 = n1 + n2 

print(n3)
print(f'{n3:.2f}\n')

print(round(n3))
print((round(n3, 2)))
