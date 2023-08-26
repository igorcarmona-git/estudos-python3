'''
.update --> Irá funciona com qualquer que tenha um iterável entre dois valores
'''

p1 = {
    'nome': 'Igor',
    'sobrenome': 'Carmona',
}

#print(p1['nome'])
print(p1.get('nome', 'Not Available')) # --> Se não tiver chave 'nome', retorna padrão 'Not available'

# nome = p1.pop('nome') # --> Elimina a chave do dicionário
# print(f'\n \n {nome}')# --> printa a chave eliminada
# print(p1)

ultima_chave = p1.popitem() #--> Elimina a ultima chave do dicts
print(f'\n \n {ultima_chave}')
print(p1)

#Forma mais comum para atualizar dict
p1.update({
    'nome': 'novo valor',
    'idade': 23,
    'Carro': True,
})

#Outra forma de atualizar dict
p1.update(moto='Suzuki', endereco='Rua Ezidio')

#Outra forma de atualizar dict usando tupla
tupla = ('fone', 'PioneerDJ'), ('CDJ', 'Pioneer 350')
p1.update(tupla)

#Outra forma de atualizar dict usando lista
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)

print(p1)
#.update --> Irá funciona com qualquer que tenha um iterável entre dois valores
