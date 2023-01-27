import requests

alvo = "https://faculdadefacec.edu.br/"

# wordlist = ["admin", "login", "portal", "css", "responsive"]
wordlist = open('prog-python/seclists/directory-list-2.3-small.txt', 'r')

requisicoes_aceitas = []

for word in wordlist:
  r = requests.get(alvo + word)
  print(f"Atacando --> {alvo + word}")

  if r.status_code == 200:
    print(f"REQUISIÇÃO ACEITA: {alvo + word}")
    requisicoes_aceitas = alvo + word
  else:
    continue

print()
wordlist.close()

print("LISTA DE REQUISIÇÕES QUE FORAM ACEITAS")
for requisicao in requisicoes_aceitas:
  print(requisicao)