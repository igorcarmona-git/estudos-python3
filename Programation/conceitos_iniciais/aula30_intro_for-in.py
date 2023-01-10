
# Não é comum usar o while em repetições finitas, onde sabemos quando terá um fim.

# É muito comum utilizar 'while True:' quando não sabemos quantas repetições teremos.
# Exemplo de uso:

senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while True:
    if senha_salva != senha_digitada:
        senha_digitada = input(f"Tentativas --> {repeticoes}x Sua senha: ")

        repeticoes += 1
        continue

    break
    

print(f"Tentativas executadas: {repeticoes}")
print("O laço tem repetições infinitas")
print()

######################################### --> Utilizando for/in <-- ############################################
# Utilizado para repetições finitas #

texto = "IGOR"
novo_texto = ""

for letra in texto: #--> o 'for' solicita para a string o meu iterador que vai armazenar cada uma das posições em 'letra'
    novo_texto += f"_{letra}"
    print(letra)

print(novo_texto)