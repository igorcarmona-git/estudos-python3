"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

print("#### --> Jogo da palavra secreta! <-- ###")

secreto = "aprendizado"
letras_acertadas = ""

tentativas = 0
num_letra = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    num_letra = len(letra_digitada)

    if num_letra > 1:
        print()
        print("ERRO --> Digite somente uma letra!")
        tentativas += 1
        continue

    if num_letra == 0:
        print()
        print("ERRO --> Você não digitou nenhuma letra!")
        tentativas += 1
        continue

    if letra_digitada in secreto:
        letras_acertadas += letra_digitada #concatenação de string

    palavra_formada = "" #Sempre que se repete o laço a palavra formada se reinicia

    for letra in secreto: #Percorre cada letra da string
        if letra in letras_acertadas: #Verifica se as letras da string estão entre as letras acertadas pelo usuário
            palavra_formada += letra #se estiver, concatenação de string
        else:
            palavra_formada += '*' #se não tiver, coloca '*' no lugar, onde não tem letra acertada

    print(f"Palavra formada: {palavra_formada}") #Colocado print fora do for para imprimir a palavra na horizontal

    if palavra_formada == secreto:
        os.system('cls') #Limpa a tela do terminal

        print("VOCÊ GANHOU!! PARABÉNS!!")
        print()
        print(f"A palavra era: {secreto}")
        print(f"O número de tentativas: {tentativas}x")

        break
