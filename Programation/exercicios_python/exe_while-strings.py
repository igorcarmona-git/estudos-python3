"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

    #Acumulação... Cria uma variavel string vazia e vai adicionando valores a essa variável.

novo_nome += '*' # Acrescenta o '*' ao final do novo_nome. 

print(novo_nome)