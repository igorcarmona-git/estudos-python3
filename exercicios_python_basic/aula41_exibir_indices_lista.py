""" 
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
################################### MINHA SOLUÇÃO ################################### 

print("MINHA SOLUÇÃO")
lista = ["Maria", "Helena", "Luiz"]

contador = -1

lista.insert(2, "Bruna")
lista.append("Igor")
lista.pop()

for nome in lista:
    contador += 1   #Cada nome recebe um número
    print(f"Posição: {contador} --> {nome}")

print()
print(lista)
print()

################################ SOLUÇÃO DO PROFESSOR #################################

print("SOLUÇÃO DO PROFESSOR")
lista1 = ["Maria", "Helena", "Luiz"]

lista1.append("João")

indices = range(len(lista1)) #Pega o tamanho da lista

for i in indices:
    print(i, lista1[i]) #printa o 'i' e printa o 'i' da lista
    
print(lista1)

