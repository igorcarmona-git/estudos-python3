nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

int_idade = 0

if idade.isdigit(): # a função 'isdigit()' checa se o usuário digitou apenas números, é uma except
    int_idade = int(idade)

if (nome and idade):
    print(f"Sua idade é: {int_idade}")
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]} ")
    
    if " " in nome:
        print("Seu nome contém espaços!")
    else:
        print("Seu nome não contém espaços!")

    print(f"Seu nome tem {len(nome)} letras!")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A última letra do seu nome é: {nome[-1]}") # Pega a ultimo indice do nome
else:
    print(f"Desculpe, você deixou campos vazios!")
