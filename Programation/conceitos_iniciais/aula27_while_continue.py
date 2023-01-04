"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue #Pula algo durante a execução do laço

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break #Para o laço de repetição

print('Acabou')

###############################################################################################
                    # Aninhamento de while

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou o outro')