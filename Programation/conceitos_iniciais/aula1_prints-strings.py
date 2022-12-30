#Aula 1 - Prints e Strings

# Para escrever comentários 

'''
Permite também escrever comentários na qual é chamado de
docString, permite pular linhas.
O interpretador faz a leitura e guarda na memória.

\r\n -> CRLF (Sistemas Windows mais antigos, serve para pular linha)
\n -> (Sistemas unix e windows mais atualizados reconhecem esse pular linha)
'''

#print(123) #Exibe algo na tela
#print(56, 78)
print(123, 345, sep=" | ", end="\n---------\n") 
print(123, 466, sep=" | ", end="\n---------\n") 
# sep é um separador de argumentos e end ao final fazer algo.

# Tudo que está dentro de aspas é um texto
print("Igor Carmona")

"""
------- Não é muito utilizado ------
#Escape (caractere -> \ )
print("Igor \"Carmona\"") 

#r (caractere -> r )
print(r"Igor \"Carmona\"") #colocar -> r | irá mostrar tbm a -> \ | no print
"""

print('Igor "Carmona"') #jeito mais utilizado





