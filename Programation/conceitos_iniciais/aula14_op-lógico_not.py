
#Operador lógico "not"

#Usado para inverter expressões

# not True => False
# not False => True

# Se usuário da enter e digita nada, string vazia => False
senha = input("Senha: ") 

# Senha = False
# Transforma em True, para executar comando.
if not senha:
    print("Você não digitou nada!")

print(not True)
print(not 0)
print(not 1)
print(not '')