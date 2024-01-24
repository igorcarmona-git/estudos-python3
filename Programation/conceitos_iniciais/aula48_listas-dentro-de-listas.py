# Lista de listas e seus índices

salas = [
    #0            1
    ["Maria", "Helena"], #0
    ["Elaine"], #1
    #0         1        2               3
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)] #2]
                                #0  1   2   3   4
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][2])

################################# Utilizando o laço 'for' ###############################
print("\n\n")

# OBS: Interessante utilizar os dados do mesmo tipo nas listas para evitar fazer uso de 'if' complicados. 

for sala in salas:
    print(f'A Sala é {sala}')
    for aluno in sala:
        print(aluno)

########################### Outro exemplo ################################

numeros = [8, 2, 3, 4]
nomes = ['Alice', 'Bob', 'Carol', 'Dave']

for numero, nome in zip(numeros, nomes):
    print(f'{numero} {nome}')