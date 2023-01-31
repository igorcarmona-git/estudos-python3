# enumerate --> Enumera iteráveis (índices), é um iterador. 

# Eles são meio que consumíveis, quando chega no último indice, encerra. 

# (0, 'Maria'), (1, 'Iago'), (2, 'Helena'), (3, 'Luiz'), (4, 'Igor') --> enumerate cria tupla com índice:valor. 
lista = ["Maria", "Helena", "Luiz"]
lista.append("Igor")
lista.insert(1, "Iago")

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

print(f"O que tem na lista enumerada:{lista_enumerada}") #Posição do ponteiro na memória da variável. 
print()

# OBS: Quando se poe enumerate em uma variável, não se pode usar mais de uma vez porque consome o seu iterador. 
#       Por isso, é usado DIRETAMENTE o "enumerate" no laço. 

############################# --> CORRETO! <-- ############################################

for item in enumerate(lista):
    print(f"Usando pela primeira vez: {item}")

print()
for item in enumerate(lista):
    print(f"Usando pela segunda vez: {item}")

##########################################################################################

# OBS: Para mostrar o enumerate em um print, você pode usar "type conversion" para uma tupla ou lista.
print()
lista2 = ["Fernando", "Gustavo", "João"]

lista2_enumerada = list(enumerate(lista2))
lista3_enumerada = list(enumerate(lista2, start=10)) #Começa a enumeração à partir do 10.

print(lista2_enumerada)
print(lista3_enumerada)
