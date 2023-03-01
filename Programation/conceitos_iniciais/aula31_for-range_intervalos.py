
""" 
for + range
range (start, stop, step) --> é um iterador, função.

"""
numeros = range(0, 50, 5)

print(numeros[1]) #-->  Você consegue pegar a posição do vetor desse iterador.
print() 

for num in numeros: #--> variável 'num' é criada, o 'for' solicita para 'numeros' seu iterador em que vai armazenar seus valores em 'num'. 
    print(num)