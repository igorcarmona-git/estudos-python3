''' 
Dentro de uma lista em Python, você pode usar uma construção chamada "list comprehension" (compreensão de lista) 
para criar uma nova lista com base em outra lista existente. Essa construção permite incluir um laço for dentro da própria lista.

'''

numeros = [1, 2, 3, 4, 5]
dobro = [numero * 2 for numero in numeros] # --> criar uma nova lista com base em outra lista existente

print(dobro)

#OBS:   A lista 'dobro' é criada usando a compreensão de lista. 
#       O laço for itera sobre cada elemento da lista numeros, multiplicando-o por 2. 


##################################### com condicional ###############################################################
numeros_gerais = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros_gerais if numero % 2 == 0] 

print(pares)

#OBS:   A compreensão de lista inclui uma cláusula condicional if para filtrar apenas os números pares.

######################################################################################################################

mensagem = "Olá, mundo!"
caracteres = [c for c in mensagem]

print(caracteres)

#OBS:   A compreensão de lista é usada para criar uma nova lista caracteres a partir da string mensagem. 
#       Em resumo, a compreensão de lista é uma técnica poderosa para criar novas listas a partir de listas existentes 
#       com transformações ou filtragem.