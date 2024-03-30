'''
Crie funções que duplicam, triplicam e quadruplicam o numero recebido como parâmetro. 
'''

# def duplica(num):
#     return num * 2

# def triplica(num):
#     return num * 3

# def quadruplica(num):
#     return num * 4

def criar_multiplicar(multiplicador): #valor que fica guardado na memória
    def multiplicar(numero): #valor dinâmico
        return numero * multiplicador
    return multiplicar 

duplicar = criar_multiplicar(2)
triplicar = criar_multiplicar(3)
quadruplicar = criar_multiplicar(4)

print()
print(criar_multiplicar(3))
print()

print(duplicar(5), duplicar(8))
print(triplicar(5))
print(quadruplicar(5)) #closure

#Pense na função criar_multiplicar como uma fábrica que produz outras funções de multiplicação. A fábrica recebe um argumento chamado multiplicador, que é como uma configuração que você decide antes de começar a produção.

#A função interna multiplicar(numero) é como um trabalhador dentro da fábrica, pronto para executar a operação de multiplicação. Esta função interna recebe um número como entrada e o multiplica pelo valor configurado anteriormente, o multiplicador.

#Então, quando você chama criar_multiplicar(2), você está configurando a fábrica para produzir funções que multiplicam por 2. Essas funções são então atribuídas às variáveis duplicar, triplicar e quadruplicar. Cada uma dessas variáveis se torna uma função específica de multiplicação.

