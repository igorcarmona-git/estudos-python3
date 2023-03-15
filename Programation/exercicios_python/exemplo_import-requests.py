# Firebase é um banco de dados online da Google, vá em Real Time database (obrigação por no final do link o .json)
# Site de APIs (Awesome API --> https://docs.awesomeapi.com.br/api-cep)
# API é um programa que alguém fez para pegar informações do site por meio de código

import requests

# PEGAR INFORMAÇÕES - GET
r = requests.get("https://testeigor-72bd5-default-rtdb.firebaseio.com/.json")
print(r)
print(r.json()) #A informação vem em forma de dicionário

# CRIAR INFORMAÇÃO - POST
info = '{"nome":"Amanda"}' #deve passar a info em formato texto
r = requests.post("https://testeigor-72bd5-default-rtdb.firebaseio.com/.json", data=info)
print(r)
print(r.json()) # Quando se faz um método post ou patch, você precisa passar os parâmetros no link do que quer criar. 

# EDITAR INFORMAÇÃO/ATUALIZAR INFORMAÇÃO - PATCH 
info = '{"nome":"Amanda", "sobrenome":"Henrique", "idade":"29"}' #deve passar a info em formato texto
r = requests.patch("https://testeigor-72bd5-default-rtdb.firebaseio.com/-NPL7CJzG1iszHhBqk9w.json", data=info)
print(r)
print(r.json())

# DELETAR INFORMAÇÃO - DELETE
r = requests.delete("https://testeigor-72bd5-default-rtdb.firebaseio.com/-NPL8QqQrRMF3k-wjhay.json")
print(r)
print(r.json())
