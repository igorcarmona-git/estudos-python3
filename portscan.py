import socket
import random

#21 --> FTP
#22 --> SSH
#80 --> HTTP
#443 --> HTTP
#445 --> SMB
#3306 --> Porta padrão serviços SQL
#25 --> Padrão SMTP

import socket

# 21 --> FTP
# 22 --> SSH
# 80 --> HTTP
# 443 --> HTTPS
# 445 --> SMB
# 3306 --> Porta padrão serviços SQL
# 25 --> Padrão SMTP

ports = [21, 22, 80, 443, 445, 3306, 25, 8080, 23, 3389, 5900]
list_ports = []
list_IPs = [
    ("lyaluno.unipar.br", "177.91.39.66"),
]

for ip_name, ip_address in list_IPs:
    print()
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        code = client.connect_ex((ip_address, port))

        if code == 0:
            print(f"{ip_name} -- ({ip_address}): {port} OPEN PORT!")
            list_ports.append((ip_name, ip_address, port))
        
        client.close()

if not list_ports:
    print("Nenhuma porta encontrada!")

#aula19min