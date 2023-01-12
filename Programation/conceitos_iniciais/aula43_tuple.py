""" 
A tupla funciona como se fosse uma lista, a diferença que a tupla é IMUTÁVEL, utilizamos quando não queremos alterar nada.
"""

nomes = ("Igor", "Iago", "Eduardo")
nomes2 = "Igor", "Iago", "Eduardo"

# OBS -->   1. Com '(' ou sem, o Python identifica como tuple, é a mesma coisa, só um jeito diferente de escrever.
#           2. Podemos converter 'tuple' para 'list', 'list' para 'tuple'.
#           3. Consegue fazer as mesmas coisas para list, menos o CRUD.

nomes = list(nomes)
print(f"LIST --> {nomes}")

nomes = tuple(nomes)
print(f"TUPLE --> {nomes}")

print()
print(nomes2)
