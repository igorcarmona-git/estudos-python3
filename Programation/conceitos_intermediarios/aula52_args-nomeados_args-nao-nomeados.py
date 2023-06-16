""" 
Argumentos nomeados e não nomeados (posicionais) em funções Python. 

Argumento nomeados tem nome com sinal de igual (nome="sem nome")
Argumento não nomeado recebe apenas o argumento (valor)

"""

# Exemplo de mal uso
def soma(x, y):
    print(f"{x=} {y=} | {x + y=}") # -> retorna 10

print(soma(5, 5)) 
soma(3, 3)
soma(y=3, x=5) #argumentos nomeados 

#Obs: Se nomear um, todos os próximos devem ser nomeados. 
#     Não é uma boa prática, usar nomeados.

#Retorna None (Porque estou colocando a função dentro de um print, que já executa um print dentro dela)