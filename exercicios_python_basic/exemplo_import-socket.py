# É uma forma de ligar o nosso código com o sistema operacional.

# A biblioteca socket permite que o sistema operacional faça alguma ação na rede. 
# Dentro da biblioteca tem toda a parte de baixo nivel que vai mexer com as conexões TCP IP, pacotes, bytes, toda parte
# realmente complicada.  

import socket 
                        #vai um socket IP   #vai ser um TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            #Passa um host e a porta para conexão
client.connect(("bancocn.com", 80))

        #envia dados a conexão          #ele espera que você envie bytes (converte a string em bytes), por isso 'b'  
client.send(b"Hello world!")

        #'recv' faz com que você receba dados dessa conexão
        #como argumento você passa a quantidade de bytes que quer receber
response = client.recv(1024)

print(response.decode()) #'decode', método dos objetos bytes que transforma o conteúdo em string

#OBS:retorna o mesmo quando você tenta fazer uma conexão com nc netcat
