
# Exercício prático sobre condicionais (if e Comparação)

n1 = input("Digite um valor: ")
n2 = input("Digite um outro valor: ")
primeiro_valor = int(n1)
segundo_valor = int(n2)

if (primeiro_valor >= segundo_valor):
    print(f"{primeiro_valor=} é maior ou igual ao {segundo_valor=}")
else:
    print(f"{segundo_valor=} é maior do que {primeiro_valor=}")