''' 
EXERCICIO --> SISTEMA DE PERGUNTAS E RESPOSTAS
'''
import os

perguntas =[
    { #0
        #chave       #valor
        'pergunta': 'Quanto é 2+2?',
        'opcoes': [1, 3, 4, 5],
        'resposta': 4,
    },
    { #1
        'pergunta': 'Quanto é 5*5?',
        'opcoes': [25, 55, 10, 51],
        'resposta': 25
    },
    { #2
        'pergunta': 'quanto é 10/2?',
        'opcoes': [4, 5, 2, 1],
        'resposta': 5,
    },
]

qtd_acertos = 0

for indice in perguntas:
    print('Pergunta: ', indice['pergunta'])
    print()

    #print na tela as opcoes disponiveis
    opcoes = indice['opcoes'] #--> valor retornado é uma lista
    for i, opcao in enumerate(opcoes, start=1):
        print(f'OPTION {i} --> {opcao}')
    print()

    escolha = input('Escolha uma opcao: ')

    acertou = False
    qtd_opcoes = len(opcoes)
    
    int_escolha = None
    if escolha.isdigit():
        int_escolha = int(escolha)
        int_escolha -= 1 #--> Feito isso por causa do print na linha 34
    
    try:
        if escolha is not None:
            if int_escolha >= 0 and int_escolha < qtd_opcoes:
                if opcoes[int_escolha] == indice['resposta']:
                    acertou = True #--> Flag
    except TypeError:
        if escolha == '':
            os.system('cls')
            print(f'Voce nao digitou nada!')
            continue

    print()
    if acertou:
        os.system('cls')
        qtd_acertos += 1
        print(f'ACERTOU! \n')
    else:
        os.system('cls')
        print(f'ERROU! \n')

#Verificação de acertos do usuário
if qtd_acertos == 0 and escolha == '':
    os.system('cls')
    print(f'Voce nao digitou nada em nenhuma das perguntas!')
elif qtd_acertos == 0:
    os.system('cls')
    print(f'Voce errou todas as perguntas!')
elif qtd_acertos == len(perguntas):
    os.system('cls')
    print(f'Voce acertou todas as perguntas!')
else:
    os.system('cls')
    print(f'Infelizmente, voce errou algumas perguntas!')

print(f'Voce acertou {qtd_acertos} de {len(perguntas)} perguntas!')