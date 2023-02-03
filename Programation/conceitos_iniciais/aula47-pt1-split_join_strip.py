"""
split e join com list e string:
    
    split -> Divide uma string em determinado caractere. (retorna uma list)
    join -> Une uma string. 
    strip --> Corta os espaços do começo e do fim da string
    rstrip --> Corta os espaços da direita da string
    lstrip --> Corta os espaços da esquerda
"""

frase = "    Olha só que,   coisa interessante   "
lista_palavras = frase.split() # função sem parâmetro, divide a string onde tiver espaços, armazenando numa lista. 
lista_frases = frase.split(',') # vai quebrar a frase em determinado caractere

print(lista_palavras)
print(lista_frases)

print("\n\n")

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip()) #As strings são imutáveis, altera seu valor na lista ao invés de diretamente na frase. 
    lista_frases[i] = lista_frases[i].strip() #A lista por ser mútavel, consegue modificar a lista. 

    #OBS: NÃO É UMA BOA PRÁTICA DE PROGRAMAÇÃO, VOCÊ MODIFICAR A LISTA DESSE JEITO. POIS, SE VOCÊ PRECISAR DA LISTA CRUA DE NOVO,
    # NÃO VAI CONSEGUIR ACESSAR. NA AULA47-PT2 ESTÁ A FORMA CORRETA. 

print(lista_frases)