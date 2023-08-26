''' 
MÉTODOS UTEIS DOS DICIONÁRIOS EM PYTHON!

len -----> quantas chaves
keys ----> iterável com as chaves
values --> iterável com os valores
items ---> iterável com chave e valores
setdefault --> adiciona valor se a chave não existe
copy ----> retorna uma cópia rasa (shallow copy)
get -----> obtém uma chave
pop -----> Apaga um item com a chave especificada (del)
popitem -> Apaga o ultimo item adicionado
update --> Atualiza um dicionário com outro
'''

pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Carmona',
    'sobrenome': 'Carmona2',
    'sobrenome': 'Carmona3' #Considera somente 2 chaves, porque voce está atualizando o valor dela e não criando uma nova. 
   #'idade': '30' 
}

pessoa.setdefault('idade', 18) #Utiliza esse valor como padrão para idade se a chave 'idade' não for declarada. Porém se ela existir, 
# o valor declarado é o que será usado (ex: 30)

print(pessoa.__len__())
print(len(pessoa))
print('\n\n')

#Dunder method --> refere-se a um conjunto especial conhecidos como "métodos mágicos" ou "métodos especiais". Esses métodos são amplamente utilizados para sobrecarregar operadores e fornecer comportamento personalizado para classes definidas pelo usuário.

print(pessoa.keys()) #retorna um dicionário de chaves
print(list(pessoa.keys())) #converte dicionário para lista
print(list(pessoa.values()))
print(list(pessoa.items()))

print('\n\n')

for valor in pessoa.values():
    print(valor)

print('\n')

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
