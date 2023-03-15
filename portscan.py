import socket

#21 --> FTP
#22 --> SSH
#80 --> HTTP
#443 --> HTTP
#445 --> SMB
#3306 --> Porta padrão serviços SQL
#25 --> Padrão SMTP

ports = [21,22,80,443,445,3306,25]
list_codes = []

for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#passa o tempo que ele vai esperar a conexão. '0.1' milisegundos
	client.settimeout(0.1)
	code = client.connect_ex(("bancocn.com", port)) #'connect_ex', retorna um inteiro, se 0 tem conexão aberta, se qualquer 
													# outra coisa, não tem conexão.
	if code == 0:
		print(f"{port} OPEN PORT!")
		list_codes.append(code)

if list_codes == []:
	print("Nenhuma porta encontrada!")

#aula19min