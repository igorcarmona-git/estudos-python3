# Operadores lógicos

# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor

# São considerados falsy (que vc já viu)
# ----> 0 0.0 '' False <-----------

# Também existe o tipo None que é usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True) # vai printar somente o que identifica como False

if 0 and 1: # 0 => considerado False, não entra na condição
    print(True and 1)

if 1 and 1:
    print(True and 1 and False) # vai printar somente o que identifica como False