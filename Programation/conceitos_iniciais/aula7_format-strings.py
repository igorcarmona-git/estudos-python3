nome = "Igor Carmona"
altura = 1.74
peso = 71
imc = peso / (altura * altura)

#formatação de strings e definição de casas decimais (f-strings)

linha1 = f"{nome} tem {altura:.2f} metros de altura"
linha2 = f"{nome} pesa {peso}kg e seu IMC é de:"
linha3 = f"----> {imc:.2f} <------"

# OBS: somente da pra definir as casas decimais usando formatação

print(linha1)
print(linha2)
print(linha3)

print()
#formatação usando o método .format

nome = "Luiz"
idade = 23
formato = '{n} tem {i:.2f} anos' #recebe os parâmetros nomeados
formato2 = '{0} tem {1} anos' #recebe a posição dos parâmetros

print(formato.format(n=nome, i=idade)) #Parâmetros nomeados
print(formato2.format(nome, idade)) #Parâmetros não nomeados