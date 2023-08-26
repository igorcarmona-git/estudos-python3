'''
SHALLOW COPY VS DEEP COPY EM DADOS MUTÁVEIS! 
'''
import copy

d1 = {
    'c1': 1,
    'c2': 2,
}

d2 = d1 #valores mutáveis ou listas

d2['c1'] = 1000
print(d1) #d1 é afetado tbm ao alterar 'd2', porque aponta para o mesmo conteúdo na memória. 

################ Exemplo de shallow copy (cópia rasa) ############################
print('\n\n')

teste1 = {
    't1': 1,
    't2': 2,
    'lista': [0, 1, 2],
}

#teste2 = teste1.copy() #shallow (rasa)
teste2 = copy.deepcopy(teste1) #copia profunda

teste2['t1'] = 800
teste2['lista'][1] = 999999

print(teste1) #Cópia rasa porque ao alterar valores mutáveis (lista), ele não consegue copiar os subníveis dessa lista e faz com que
#altere o valor da lista no 'teste1'. 

print(teste2)

#OBSERVACOES: 
#   Valores mutáveis são objetos cujo estado interno pode ser modificado após a sua criação. 
#   Isso significa que você pode fazer alterações nos valores sem criar um novo objeto. EX:

                                # lista = [1, 2, 3]
                                # lista.append(4)  # Modifica a lista existente
                                # print(lista)  # Output: [1, 2, 3, 4]


#   Valores imutáveis são objetos cujo estado interno não pode ser alterado após a sua criação. 
#   Isso significa que, quando você faz uma alteração em um valor imutável, na verdade está criando um novo objeto com o valor modificado.

                                # x = 10
                                # y = x + 5  # Cria um novo objeto com o valor 15
                                # print(y)  # Output: 15
