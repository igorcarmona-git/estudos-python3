import socket

# Nome do DNS a ser pesquisado
dns = "www.unipar.com.br"

# Realiza a pesquisa DNS reversa e armazena a lista de endereços IP
ip_list = socket.getaddrinfo(dns, None, socket.AF_INET)

# Imprime cada endereço IP encontrado
for ip in ip_list:
    print(ip[4][0])

