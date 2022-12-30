""" 
Introdução ao try/except
try --> tentar executar o código
except --> ocorreu algum erro ao tentar executar

"""

idade = input("Digite a sua idade: ")

# a função 'isdigit()' checa se o usuário digitou apenas números. 
if idade.isdigit(): 
    int_idade = int(idade)
else:
    print(f"Isso não é um número!")

# OBS: Erros são exceções no python. 

numero_str = input("Vou dobrar o número que vc digitar: ")

# fail-fast
try: 
    numero_float = float(numero_str)
    print(f"FLOAT: {numero_float}")
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

"""
try/except --> 'try' tenta executar determinado código caso ocorra qualquer erro, com a sintaxe escrita certinha, você consegue
                capturar esse erro e fazer o que quiser depois.

if e else são para lógica, try/except são para erros (exceptions).
Ambos podem fazer a mesma coisa em várias ocasiões, mas seu uso é como descrevi acima.
"""

