import dns.resolver
import random
import time

res = dns.resolver.Resolver()
arquivo = open("seclists/directory-list-2.3-small.txt", "r")

#		método ler arquivo 			separa o conteudo por linhas
subdominios = arquivo.read().splitlines()

alvo = "lyaluno.unipar.br"

for subdominio in subdominios:
	# Se der erro no retorno do resultado, ele pula e vai pro proximo subdominio. 
	try:
		sub_alvo = subdominio + "." + alvo
		resultado = res.resolve(sub_alvo, "A") # retorna um objeto, o IP do subdominio

		time.sleep(random.randint(3, 600))

		#Por ser um objeto, é possível interar sobre a variável
		for ip in resultado:
			print(sub_alvo, "->", ip)
	except:
		pass

