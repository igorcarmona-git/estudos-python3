# Desempacotamento

lista = ["Maria", "Helena", "Luiz"]
lista.append("Igor")
lista.insert(1, "Iago")

for indice, nome in enumerate(lista): #Jeito mais fácil de desempacotar tupla ou lista
    print(indice, nome)

print()

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

print() 

# (0, 'Maria'), (1, 'Iago'), (2, 'Helena'), (3, 'Luiz'), (4, 'Igor')
for tupla_enumerada in enumerate(lista): #Percorre cada tupla
    print("FOR da tupla:")
    for valor in tupla_enumerada: #Percorre cada valor de uma tupla e printa na tela
        print(f"\t{valor}")

#OBS: Quer dizer tudo a mesma coisa. 
#   "\t" é usado para fazer tabulação no print. 