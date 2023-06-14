""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+, -, /, *): ')

    numeros_validos = None # Flag

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue #Volta para o começo do laço while

    operadores_permitidos = '+-/*'

    ################################################## CONDICIONAIS DE VALIDAÇÃO ############################################################

    # Verifica se o que os operadores que usuário digitou não estiver entre os permitidos.  
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    # Verifica se o usuário digitou mais de um operador para o cálculo. 
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ##############################################################################################################################################

    print('Realizando a sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
    else:
        print('Algum possível erro de verificação bypassou...')

    #lower --> Transforma o que usuário digita em minusculo
    #startswith --> Verifica se o que usuário digitou começa com 's'
    sair = input('Quer sair? [s]im: ').lower().startswith('s') 

    if sair is True:
        break   #Sai do laço while