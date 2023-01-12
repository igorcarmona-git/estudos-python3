# OBS -->   Quando um valor IMUTÁVEL estou copiando o valor quando uso '='
#           Quando um valor MUTÁVEL estou apontando para o mesmo valor na memória '=' 


lista_a = ["luiz", "Maria"]
lista_b = lista_a 

lista_a[0] = "Qualquer coisa"
print(lista_b) # --> A 'lista_b' é alterada, porque aponta para 'lista_a' onde ela foi alterado o valor na memória

print()
################################ Usando método .copy() #############################################
print()

lista_1 = ['Luiz', 'Maria', 1, True, 1.2]
lista_2 = lista_1.copy() # --> .copy() copia os valores da 'lista_1', cria uma nova lista e coloca em 'lista_2'

lista_1[0] = 'Qualquer coisa'
print(lista_1)
print(lista_2) # Lista não foi afetada, pq é outra lista que está na memória, temos duas listas separadas 