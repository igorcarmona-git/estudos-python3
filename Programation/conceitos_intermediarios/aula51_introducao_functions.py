"""
Introdução às funções (def) em python

Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor especifico. 

Por padrão, funções Python retornam None (nada). 
"""

###################### Exemplos: ########################################################

#def saudacao(nome):
#    print(f"Olá, tudo bem? {nome}")

#def saudacao():
#    print(f"Olá, tudo bem?)

def saudacao(nome="Sem nome"):
    print(f"Olá, tudo bem? {nome}")

saudacao("Igor")
saudacao()

###################################################################################

def multiplo_de(numero, multiplo):
    resultado = (numero % multiplo) == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)

# É possível chamar funções sem parâmetro, ja definindo um valor direto nos parâmetros