''' 
MÉTODOS UTEIS:
    add, update, clear, discard
'''

#add:
s1 = set()
s1.add('igor')

#update: 
# (parecido com add, mas é geralmente utilizado para mandar varios valores)
# update, se não passar em forma de tupla itera sobre cada iterável da String

s1.update('Carmona') 
#--> saida: {'n', 'a', 'C', 'o', 'r', 'm', 'igor'}

s1.update(('Carmona', 'Fernando', 'Gustavo', 30)) 
#--> saida: {'o', 'Fernando', 'r', 'igor', 'n', 'C', 'm', 30, 'Carmona', 'Gustavo', 'a'}

#discard: (Passa o valor que quer discartar como parametro)
s1.discard('Gustavo')
s1.discard(30)
print(s1)

#clear:
s1.clear()
print(s1)
