# Interpolação básica de strings

# s --> string
# d | i --> int
# f --> float
# x | X --> Hexadecimal (ABCDEF0123456789) --> As diferenças de x e X, é que no print sai maiusculo ou não. 

nome = "Igor"
preco = 1000.9456775
variavel = "%s, o preço é R$%.2f" % (nome, preco)

print(variavel)
print("O hexadecimal de %d é %04X" % (1500, 1500))

# OBS: Para substituir isso, temos 3 estratégias e escolher qual quer usar: f-strings, format, interpolação. 
# O professor mais usa o f-strings. 