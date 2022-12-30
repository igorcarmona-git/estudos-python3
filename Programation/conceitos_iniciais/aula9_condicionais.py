#if  / elif      / else
#se / se não se/ se não

entrada = input("Você quer 'entrar' ou 'sair'? ")

if entrada == "entrar":
    print("Você entrou no sistema!")
    print("igor carmona system")
elif entrada == "sair":
    print("Você saiu do sistema!")
else:
    print("Você não digitou nenhuma das opções!")
    entrada = input("Você quer 'entrar' ou 'sair'? ")

    if entrada == "entrar":
        print("Você entrou no sistema!")
        print("igor carmona system")
    else:
        print("Você saiu do sistema!")
print()
print("################################################################################################")
print()

# Se você quiser que o interpretador pule a leitura de algo, digite '...' => Elipses ou digite 'pass'!

condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    print("Código para condição 1")
    print("Código para condição 1")
elif condicao2:
    print("Código para condição 2")
elif condicao3:
    print("Código para condição 3")
elif condicao4:
    print("Código para condição 4")
else:
    print("Nenhuma condição foi satisfeita!")

# Voce pode fazer um "Run and Debug" para ver o que está acontecendo no seu código
# Perto dos números de linhas há bolinhas vermelhas, significa "breakpoints", é onde,
# o interpretador irá parar de fazer o debug. 

# Selecione o tipo de arquivo a ser debugado e de run
# Quando estiver executando irá msotrar comandos no superior da tela sobre pular linha a linha e etc 