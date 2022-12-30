"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a  --> Chama os métodos: repr, str, asci 
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}') # Não vai chegar a usar formatação complicada assim, mas é interessante saber que existe
print(f'{1000.4873648123746:+,.2f}') # Se o número for positivo, vai acrescentar o sinal de '+'
print(f'O hexadecimal de 1500 é {1500:04X}')
print(f'{variavel!r}') 