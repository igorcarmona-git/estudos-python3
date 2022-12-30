adicao = 10 + 10
subtracao = 10 - 5
multiplicacao = 5*5
divisao = 10 / 2.2
divisao_inteira = 10 // 2.2
exponenciacao = 2 ** 10
modulo = (25 % 5) #resto da divisão

print("Adição:", adicao)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão Inteira:", divisao_inteira)
print("Exponenciação:", exponenciacao)
print("Módulo:", modulo)

print()
print("Peculiaridades das operações matemáticas")
print()

concatenacao = "Igor" + " " + "Carmona"
print(concatenacao)

a_dez_vezes = "A" * 10
tres_vezes_igor = 3 * "Igor"
print(a_dez_vezes)
print(tres_vezes_igor)

print()
print("Ordem de precedência das operações")
print()

'''
ordem:
1 -> (n+n)
2 -> **
3 -> * / // %
4 -> + -
'''

conta = (1 + int(0.5 + 0.5)) ** (5+5) #exemplo 1
conta2 = (1+1) ** (5+5) #exemplo 2
print(conta)
print(conta2)