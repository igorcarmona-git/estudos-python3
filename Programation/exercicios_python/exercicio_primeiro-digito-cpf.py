"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10.

Ex.: 745.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2 
*   7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
     resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
digitos = input("Digite o seu CPF: ")

digitosFinais = [] 

if len(digitos) > 9:
    for finais in digitos[9:]:
        digitosFinais.append(finais)

lista_coletaDigitos = []

for digito in digitos:
    if (len(digito) <= 1 and len(digito) >= 0):
        int_coletaDigitos = int(digito)
        lista_coletaDigitos.append(int_coletaDigitos)

lista_coletaDigitos.pop()
lista_coletaDigitos.pop()

list_multiplicacao = []

cont = 0
num = 10

while num >= 2:
    total = num * lista_coletaDigitos[cont]
    list_multiplicacao.append(total)
    num -= 1

    if cont > 9:
        break

    cont += 1

cont = 0
soma = 0
resultado = 0

for num in list_multiplicacao:
    soma += list_multiplicacao[cont]
    resultado = soma

    cont += 1

resultado *= 10
restoDivisao = resultado % 11

if restoDivisao > 9:
    total = 0
else:
    total = restoDivisao

print(restoDivisao)





