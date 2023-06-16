""" 
ESCOPO DE FUNÇÕES EM PYTHON

Escopo significa o local onde aquele código pode atingir, existe escopo global e local. 

O Escopo global é o espaço onde todo o código é alcançavel
O Escopo Local é o espaço onde apenas nomes do mesmo local podem ser alcançados
"""

#####################################################################

x = 1

def escopo():
    global x # --> permite que eu manipule a variavel definida globalmente (NÃO É UMA BOA PRÁTICA DE PROGRAMAÇÃO, IMPORTANTE SABER)
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x, y) # --> pega o 'x' definido no 'escopo()', o 'x' é protegido e executado somente dentro do 'escopo()'
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)

#Obs: Preste atenção na ordem de execução das funcoes. 
#       x é variavel global (se não declarada dentro da função)
#       y é variavel local e somente é vista dentro da funcao "outra_funcao()"

# CALL STACK --> Pilha de chamadas (onde guarda as informações na memória), consegue visualizar ele no Debugger. 