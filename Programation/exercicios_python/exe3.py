"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite o seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 0:
    print(f"Você não digitou nenhum nome!")

if tamanho_nome <= 4 and tamanho_nome > 0:
    print(f"Seu nome {nome} é curto!")

if tamanho_nome >= 5 and tamanho_nome <= 6:
    print(f"O seu nome {nome} é normal!")

if tamanho_nome > 6:
    print(f"Seu nome {nome} é muito grande!") 