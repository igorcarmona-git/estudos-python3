''' 
EXEMPLO DE USO DOS SETS:)
'''

letra_digitada = set()

while True:
    letra = input('Digite: ')
    letra_digitada.add(letra.lower())

    if 'd' in letra_digitada:
        print('Parabens, voce achou a letra!')
        break

    print(letra_digitada)