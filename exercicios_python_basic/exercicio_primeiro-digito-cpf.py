"""
CÁLCULO DO PRIMEIRO DIGITO DO CPF.

CPF: 746.824.890-70
Colete a soma1 dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contador1agem regressiva começando de 10.

Ex.: 745.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2 
*   7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultado1s:
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado1 anterior por 10
301 * 10 = 3010

Obter o resto da divisão da contador1a anterior por 11
3010 % 11 = 7

Se o resultado1 anterior for maior que 9:
    resultado1 é 0
contador1rário disso:
     resultado1 é o valor da contador1a

O primeiro dígito do CPF é 7
"""

print(f"Solução pessoal IGOR \n\n")

digitos1 = input("Digite o seu CPF: ")

if digitos1 == '':
    print(f"Você não digitou nada! Digite um CPF.\n")
    exit()
elif not digitos1.isdigit():
    print("Você digitou apenas letras! Digite somente números de um CPF válido.")
    exit()
elif len(digitos1) < 11:
    print("Você digitou números insuficientes para ser um CPF válido. Digite novamente!")
    exit()
elif len(digitos1) > 11:
    print("Você digitou números acima do permitido! Digite um CPF válido!")
    exit()

digitos1Finais1 = [] 

if len(digitos1) > 9:
    for finais in digitos1[9:]:
        digitos1Finais1.append(finais)

lista_coletaDigitos1 = []

for digito in digitos1:
    if (len(digito) <= 1 and len(digito) >= 0):
        int_coletaDigitos1 = int(digito)
        lista_coletaDigitos1.append(int_coletaDigitos1)

lista_coletaDigitos1.pop()
lista_coletaDigitos1.pop()

list_multiplicacao1 = []

contador1 = 0
num1 = 10

while num1 >= 2:
    total1 = num1 * lista_coletaDigitos1[contador1]
    list_multiplicacao1.append(total1)
    num1 -= 1

    if contador1 > 9:
        break

    contador1 += 1

contador1 = 0
soma1 = 0
resultado1 = 0

for num1 in list_multiplicacao1:
    soma1 += list_multiplicacao1[contador1]
    resultado1 = soma1

    contador1 += 1

resultado1 *= 10
restoDivisao1 = resultado1 % 11

if restoDivisao1 > 9:
    total1 = 0
    print(f"CPF INVÁLIDO! {total1}")
    exit()
else:
    total1 = restoDivisao1
    total_primeiro_digito = total1

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

lista_coletaDigitos2 = []

for digito2 in digitos1:
    if (len(digito2) <= 1 and len(digito2) >= 0):
        int_coletaDigitos2 = int(digito2)
        lista_coletaDigitos2.append(int_coletaDigitos2)
    
lista_coletaDigitos2.pop()
lista_coletaDigitos2.pop()

# Quase igual o calculo do primeiro digito, o que muda que você coloca o valor total do primeiro digito. 
lista_coletaDigitos2.append(total_primeiro_digito)

list_multiplicacao2 = []
contador2 = 0
num2 = 11

while num2 >= 2:
    total2 = num2 * lista_coletaDigitos2[contador2]
    list_multiplicacao2.append(total2)
    num2 -= 1

    if contador2 > 10:
        break

    contador2 += 1

contador2 = 0
soma2 = 0
resultado2 = 0

for num2 in list_multiplicacao2:
    soma2 += list_multiplicacao2[contador2]
    resultado2 = soma2

    contador2 += 1

resultado2 *= 10
restoDivisao2 = resultado2 % 11

if restoDivisao2 > 9:
    total2 = 0
    total_segundo_digito = total2
    print("CPF VÁLIDO!")
else:
    print(f"CPF INVÁLIDO!")
    exit()



