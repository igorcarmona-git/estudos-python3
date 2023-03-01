"""
Introdução ao desempacotamento

OBS:    1. Caso coloque mais variáveis do que valores, ocorre erro. (O mesmo vale, se for ao contrário)
        2. Muito usado '_' entre os desenvolvedores para indicar que uma variável está criada, mas não vai ser utilizada
        3. Utiliza-se '*' para pegar e armazenar o restante dos itens que não forem usados na desempacotação
"""

nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]
print(nome2)

nome1, *_ = ["Maria", "Helena", "Luiz"]
print(nome1, _) #'_' --> printa uma nova lista com o restante não desempacotado

_, nome2, *_ = ["Maria", "Helena", "Luiz"]
print(nome2, _)

######################### Outro exemplo #####################################################################################

string = 'ABCD'
lista = ['Fernando', 'Gustavo', 1, 2, 3, 'Igor']
tupla = ('Python', 'é', 'legal')

primeiro, segundo, *_, antiPenultimo, ultimo = lista 
print(primeiro, ultimo, antiPenultimo)
print(f"Aqui eu estou pegando o resto: {_}")

##################################################################################################################################
########################### --> Desempacotamento em chamadas de métodos e funções <-- ############################################

print("\n")

salas = [
    #0            1
    ["Maria", "Helena"], #0
    ["Elaine"], #1
    #0         1        2            
    ["Luiz", "João", "Eduarda"] #2]
]

string = 'ABCD'
lista = ['Fernando', 'Gustavo', 1, 2, 3, 'Igor']

print(*salas) #Passa lista por lista para dentro do print
print(*lista) # Passa um argumento de cada vez para dentro do print
print(*string) #Passa caractere por caractere para dentro do print

print('\n')

print(*salas, sep='\n') #Passa lista por lista para dentro do print e separa elas pulando linha