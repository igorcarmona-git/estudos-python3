"""
Flag (Bandeira) --> Marcar um local
None --> Não valor
is e is not --> é ou não é (tipo, valor, identidade)

"""

condicao = True
passou_no_if = None # Flag

if condicao:
    passou_no_if = True 
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None: # Checa se a variável passou_no_if se ela está None ainda. (True)
    print('Não passou no if')
else:
    print('Passou no if')

# OBS: Pense que estamos ficando uma bandeira em determinado local do código (passou_no_if), a gente utiliza o 'None' para dizer,
# se a variável tem ou não tem valor, essa bandeira ta fincada ou não ta fincada. 