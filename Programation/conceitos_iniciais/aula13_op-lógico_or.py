# Operadores lógicos

# or -> Qualquer condição verdadeira avalia toda a expressão como verdadeira. 
#       Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor

# São considerados falsy (que vc já viu)
# ----> 0 0.0 '' False <-----------

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True or False or 0)  
print(0 or False or 0 or 'abc'or True) # identifica o primeiro que for True. 

#exemplo de if usando 'or'
senha = input("Senha: ") or "Sem senha" # string vazia é considera False, e string cheia é considera True, executa True
print(senha)