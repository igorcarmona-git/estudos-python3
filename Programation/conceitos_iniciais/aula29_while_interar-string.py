frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum"

# Função '.count' --> faz a contagem de caracteres, palavras, etc... 
print(frase.count('a'))

#### usando while (iterando na string) ####

frase = 'aaaa ooo'

i = 0
qtd_salvo = 0
letra_salvo = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1  #Se não incrementar antes do "continue", ele nunca irá incrementar o 'i', entra no loop infinito.
        continue #Volta para o ínicio do laço while

    qtd_atual = frase.count(letra_atual) #conta quantas vezes aparece a letra na frase

    if qtd_salvo <= qtd_atual:
        qtd_salvo = qtd_atual
        letra_salvo = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_salvo}" que apareceu {qtd_salvo}x')


