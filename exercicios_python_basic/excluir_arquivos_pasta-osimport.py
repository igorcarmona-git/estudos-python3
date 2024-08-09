
# os.rmdir --> Para remover diretórios vazios
# shutil.rmtree --> remover diretórios com arquivos
# os.remove --> remove arquivos, voce precisa estar na pasta. 
# os.environ --> Traz informações do sistema em dicionário chave:valor
# os.getcwd --> Traz info sobre o local da pasta em que você está
# os.chdir --> Permite você navegar entre os diretórios
# os.listdir --> Lista tudo o que tem dentro de um diretório
# os.makedirs --> Cria pasta com subpastas ao passar o caminho. 
# os.rmdir --> remove diretórios, somente se a pasta estiver vazia. 
# os.startfile --> Abre um arquivo ao executar.
# os.rename --> Renomeia os nomes dos arquivos.
# os.walk --> ele lista as pastas de forma mais eficiente. 

###################### path é um submódulo da biblioteca OS ###########################################################

# os.path.commonpath([caminho1, caminho2]) --> Retorna o que é comum entre os dois caminhos
# os.path.join() --> Junta strings para formar uma string final

import os
import shutil

caminho = r'C:\Users\igorc\Documents\Teste' #'r' evita que o python leia o caractere de forma especial
os.chdir(caminho)

# os.startfile(r"C:\Users\igorc\Documents\Teste\LEIA-ME.txt")

if os.getcwd() == caminho:
    for root, dirs, files in os.walk(caminho):
        try:     
            shutil.rmtree(root) #Exclui arquivos com diretórios de forma recursiva
        except PermissionError:
            print(os.getcwd())
            continue
else:
    print("Por favor, entre no caminho correto!")

