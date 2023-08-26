'''
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn.

sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

############################# CRIANDO UM set #####################
set(iterável) ou {1, 2, 3}
'''

s1 = set() #vazio
s1 = {'Igor', 1, 2, 3} #com dados
s2 = set('Igor')

print(s2) #--> Não garante a ordem dos elementos, mas itera sobre eles