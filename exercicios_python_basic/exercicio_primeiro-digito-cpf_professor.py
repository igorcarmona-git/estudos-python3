"""
CÁLCULO DO PRIMEIRO DIGITO DO CPF.

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

cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo1 = 10

resultado_digito1 = 0

for digito in nove_digitos:
    resultado_digito1 += int(digito) * contador_regressivo1
    contador_regressivo1 -= 1

total_digito1 = ((resultado_digito1 * 10) % 11)

#Operação ternária
total_digito1 = total_digito1 if total_digito1 <= 9 else 0
print(total_digito1)