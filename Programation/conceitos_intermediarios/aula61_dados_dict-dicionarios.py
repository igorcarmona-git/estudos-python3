''' 
--> DICIONÁRIOS EM PYTHON (TIPO dict) <--

- Dicionários são estruturas de dados do tipo de "chave" e "valor". 

- Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc...
- O valor pode ser de qualquer, incluindo outro dicionário.

- Usamos as chaves {} ou a classe dict para criar dicionários, conforme os exemplos abaixo.

- Imutáveis: str, int, float, bool, tuple
- Mutável: dict, list
'''

#Forma mais usada para criar dicionários
pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Carmona',
}

#Forma menos usada para criar dicionários
pessoa2 = dict(
    nome = 'Igor',
    sobrenome = 'Carmona'
)

print(pessoa['nome'])
print(pessoa2['nome'])

########################################################################################################
#Voce pode utilizar dicionarios para coisas em que tenha vários atributos. Ex: Produto, Pessoa etc. 
pessoa3 = {
    'nome': 'Igor',
    'sobrenome': 'Carmona',
    'idade': 23,
    'altura': 1.7,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 110},
        {'rua2': 'outra rua', 'numero': 126},
    ],
}
print()

#Voce pode printar acessando os campos especificos
print(pessoa3['enderecos'], type(pessoa3))
print(pessoa3['enderecos'][0])
print(pessoa3['enderecos'][1])

print()

#Voce pode utilizar a leitura do dicionario também em laço:
for chave in pessoa3:
    print(chave, pessoa3[chave]) #'pessoa3[chave] --> retorna o valor de dentro da chave'