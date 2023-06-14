""" 
Faça uma lista de compras com listas.

O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.

Não permita que o programa quebre com  erros de índices inexistentes na lista.
"""
import os

print("MINHA LISTA DE COMPRAS \n")

lista_compras = []

while True:
    print("Selecione uma opção!")
    print("[1] INSERIR | [2] APAGAR | [3] LISTAR | [4] SAIR \n")

    inserir = None
    apagar = None
    listar = None 
    int_tecla = 0
    tamanho_lista_compras = len(lista_compras)

    try:
        tecla = input("Digite o número: ")
        int_tecla = int(tecla)

        os.system('cls')

        if int_tecla == 1:
            inserir = input("Valor: ")

            if inserir.isdigit():
                print(f"\n\tDigite apenas NOMES de produtos!\n")
                continue
            elif inserir == "":
                print(f"\n\tVocê não digitou nada, digite algum produto!\n")
                continue

            lista_compras.append(inserir)
            continue
        elif int_tecla == 2:
            if lista_compras == []:
                print("\n\tNão tem NENHUM valor na lista!\n")
                continue
            
            print("\nSua lista de compras atualizada! \n")
            indice = 1      #Print da lista dos indices para o usuário a partir do 1
            for item in lista_compras:
                print(f"\t{indice} - {item}\n")
                indice += 1

            apagar = input("Escolha o índice que deseja apagar: ")
            int_apagar = int(apagar)
            
            if int_apagar > tamanho_lista_compras:
                print("\n\tVocê digitou indices que não estão na lista!\n")
                continue
            elif int_apagar <= 0:
                print("\n\tVocê digitou indices que não estão na lista!\n")
                continue

            print(f"\t\nO produto: '{lista_compras[int_apagar - 1]}' foi apagado com sucesso! \n")       #[int_apagar - 1] --> Porque os indices para o usuário começa do 1, mas lista em si não, começa do 0
            del lista_compras[int_apagar - 1]        # Usuário apaga 1, mas na verdade ta apagando indice 0
            continue
        elif int_tecla == 3:
            if lista_compras == []:
                print("\n\tNão tem NENHUM valor para ser listado!\n")
                continue

            print("\nSua lista de compras atualizada! \n")
            indice = 1
            for item in lista_compras:
                print(f"\t{indice} - {item}\n")
                indice += 1
            continue
        elif int_tecla == 4:
            print("\nVocê saiu do programa!\n")
            break
        else:
            print("\n\tPor favor! Digite um número das opções válido!\n")
    except ValueError:
        os.system('cls')
        print("\t\nVocê não digitou nada!\n")       

##########################################################################################################################

# OBS: try e except posso tratar erros especificos, posso usar varios except. 
