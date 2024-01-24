
"""
https://docs.python.org/pt-br/3/library/stdtypes.html --> Documentação Python
Imutáveis que vimos: str, int, float, bool
"""

string = 'Luiz Otávio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'

print(string)
print(outra_variavel)
print(len(string))



print(string.zfill(12)) #Preenche com zeros os campos livres da string

#Se o tamanho da string é 11, vai começar apenas a preencher os zeros, somente depois do tamanho dela.