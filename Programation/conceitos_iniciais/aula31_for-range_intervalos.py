
""" 
for + range
range (start, stop, step) --> é um iterador, função.

"""
list_num = []

numeros = range(0, 50, 5)
print(type(numeros))

print(numeros[1]) #-->  Você consegue pegar a posição do vetor desse iterador.
print() 

for num in numeros: #--> variável 'num' é criada, o 'for' solicita para 'numeros' seu iterador em que vai armazenar seus valores em 'num'. 
    list_num.append(num)
    print(num)

print(list_num)