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

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5)) #closure

