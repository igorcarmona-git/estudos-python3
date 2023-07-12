''' 
Termos técnicos: Higher Order Functions e First-Class Functions
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

#Higher Order Functions --> Funções que podem receber e/ou retornar outras funções

#First-Class Functions --> Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas é importante saber.
Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
'''

def saudacao(msg):
    return msg 

def executa(funcao, texto):
    return funcao(texto) #Passa uma funcao qualquer e qualquer coisa junto

saudacao2 = saudacao #Variável aponta para a função armazenada na memória

exe = executa(saudacao2, 'Bom dia') #chama a função "executa" passando como parametro uma função e um texto
print(exe)

############################# Exemplo 2 ########################################################
print('\n\n')

def mensagem(msg, nome):
    return f'{msg}, {nome}!'

def executa2(funcao, *args):
    return funcao(*args)

print(executa2(mensagem,'Boa noite!', 'Igor')) 