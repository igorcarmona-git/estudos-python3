"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break #Procura o laço de repetição mais próximo e para o laço.

print('Acabou')

contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1

print('Acabou o outro')