############################ Cálculo primeiro digito #################################

print("Não coloque traços e nem pontos, somente numeros!")
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

#################### Cálculo segundo digito ##############################

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