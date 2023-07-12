"""
Closure e funções que retornam outras funções
"""

#closure (valores ficam na memória)
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

#Executa função assim que é chamada (sem closure)
# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     return saudar()

say_morning = criar_saudacao('Bom dia')
say_goodnight = criar_saudacao('Boa noite')

print(say_goodnight('nomequalquer')) #closure

for nome in ['Igor', 'Fernando', 'Gustavo', 'Henrique', 'Kleber', 'Daiane']:
    print(say_morning(nome)) #closure --> para ter algum valor retornado, a função precisa ser fechada. (Adiando os valores para a funcao)
    print(say_goodnight(nome))

# OBS: Com closure, enquanto a função não é fechada, ele guarda o valor na memória até a função ser fechada, fazendo com que force o 
#      Python a guardar os valores para resolver ela depois. 

# Isso tipo de coisa é utilizado em paradigma de programação funcional 