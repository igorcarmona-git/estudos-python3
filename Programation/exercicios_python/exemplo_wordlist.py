import requests

alvo = "https://cianorte.pr.gov.br/"

wordlist = ["admin", "login", "portal", "css", "responsive"]

for word in wordlist:
  r = requests.get(alvo + word)
  print(f"Atacando --> {alvo + word}")

  if r.status_code == 200:
    print("Eu tenho!")

  if r.status_code != 200:
    print(f"Não tem! {alvo+word}")
    print(f"ERRO: {r.status_code}")

  print()