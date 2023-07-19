'''
MANIPULANDO CHAVES E VALORES EM DICIONÁRIOS!
'''

pessoa = {}

####
####

pessoa['nome'] = 'Igor Carmona'
pessoa['sobrenome'] = 'Carmona'

print(pessoa)
print(pessoa['nome']) # Ao tentar acessar uma chave que não existe no dicionário voce terá um KeyError. 

del pessoa['sobrenome'] #Voce pode apagar chaves e dicionários
# del pessoa
print(pessoa)

print('\n\n')
####################### Chave dinâmica ##############

pessoa2 = {}

chave = 'nome_completo'
pessoa2[chave] = 'Igor Ortega Carmona'

print(pessoa2[chave])

#############################################################################################
#'.get' --> permite voce saber se a chave existe ou não. 

if pessoa2.get('nome_completo') is None: #Por padrão, retorna 'None' se a chave não existir
    print('Não Existe!')

#Obs: Se voce não usar o get, fazer algo do tipo if pessoa2['sobrenome'], não para a exceção se não existir a chave, seu programa vai
#acusar um erro de KeyError. 