""" 
Valores padrão para parâmetros

Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado. 
"""

def soma(x, y):
    print(x, y)

######################### Exemplo de refatoração de código ############################
"""
Vamos supor que construímos nosso código e queremos mudar algo dentro dele, alguma função por exemplo, 
mas sem prejudicar o restante do código.
"""

#jeito errado
# def soma2(x, y, z=0):
#     if z: ---> Se usuário passar 0, Vai considerar False e não imprime o 0. 
#         print(f"{x=} {y=} {z=}", x + y + z)
#     else:
#         print(f"{x=} {y=}", x + y)

#jeito certo
                #valor padrão
def soma2(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)

soma2(10, 10)
soma2(3, 5)
soma2(30, 30, 30)