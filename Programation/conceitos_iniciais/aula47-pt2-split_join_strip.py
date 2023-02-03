"""
split e join com list e string:
    
    split -> Divide uma string em determinado caractere. (retorna uma list)
    join -> Une uma string. 
"""

############## JEITO CORRETO DE TER UMA LISTA SEM MODIFICAR A LISTA CRUA #######################

frase = "    Olha só que,   coisa interessante   "
listaFrasesCruas = frase.split(',')

listaFrases = []

for i, frase in enumerate(listaFrasesCruas):
    listaFrases.append(listaFrasesCruas[i].strip())

print(listaFrasesCruas)
print(listaFrases) #Você gera uma nova lista embaixo, tendo a possibilidade de saber os valores da lista antiga. (jeito correto)

######################### join (unir strings) ###################################################

frases_unidas = '-'.join('abc') # "'seperador'.join(iterável)" --> Somente iteráveis (list, tuples, strings)
frases_unidas = ' --> '.join(listaFrases)
print(frases_unidas)