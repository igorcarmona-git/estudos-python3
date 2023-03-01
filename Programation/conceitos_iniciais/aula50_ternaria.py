"""
Operação ternária (Condicional de uma linha)
<valor> if <condição> else <outro valor> 
"""
# Valor se a condição for falsa, senão outro
print('Valor' if False else 'Outro Valor')

# Valor se a condição for verdadeira, senão outro
condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)

################## Exemplo para digito de CPF ####################
print("\n\n")


digito = 9
novoDigito = digito if (digito <= 9 and digito >= 0) else 0
novoDigito2 = 0 if (digito > 9 and digito <= 0) else digito # Condição ternária ao contrário
print(novoDigito)
print(novoDigito2)

# É possével fazer o seguinte (Mas não recomendado!)

print('Valor' if True else 'Outro valor' if True else 'Fim')
# Vai ser 'Valor' se for verdadeiro, senão será 'Outro valor' e será somente 'Outro valor' se for verdadeiro, senão será 'Fim'
