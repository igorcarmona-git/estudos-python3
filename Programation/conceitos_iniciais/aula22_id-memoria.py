"""
id --> identidade (Busca o valor da memória da variável)

"""

v1 = 'a'
v2 = 'b'
v3 = 'a'

print(id(v1)) 
print(id(v2))
print(id(v3))

# OBS: 'v1' e 'v2' por ter valores iguais, o Python entende que pode ter o mesmo valor na memória,
#       então, o valor é igual na memória. Apenas 'v2' tem valor diferente na memória. 