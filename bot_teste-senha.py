import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from unidecode import unidecode

#Configurations
options = Options()
options.add_argument('window-size=1280x720')
#options.add_argument('--headless')

#Default Code
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

#Full code building
def resetSenha(list_emails_atualizada):
    navegador.get('https://www.passaportevip.com/cineteatro/login.html')
    time.sleep(3)

    while True:
        botao_reset = navegador.find_element(By.XPATH, '//*[@id="jaCadastradoForm"]/div[1]')
        botao_reset.click()
        time.sleep(3)

        for nome in list_emails_atualizada:       
            campo_email = navegador.find_element(By.XPATH, '//*[@id="esqueciSenhaForm"]/div[1]/div[3]/input[1]')
            campo_email.send_keys(f'{nome}equinel2@gmail.com')
            campo_email.submit()

            time.sleep(3)

            try:
                mensagem_erro = navegador.find_element(By.NAME, 'Foi enviado para seu e-mail *****equinel2@gmail.com as instruções para a recuperação da sua senha.')
                print(mensagem_erro)
                print(f'{nome}equinel2@gmail.com')
            except NoSuchElementException:
                pass
        break

list_emails = open('C:\\Users\\igorc\\Pictures\\listemails.txt', 'r', encoding='utf-8')
list_emails_atualizada = []

for linha in list_emails:
    texto = linha.strip().lower() #strip --> Corta os espaços do começo e do fim da string | lower --> deixa toda a linha minuscula
    texto = unidecode(texto)

    list_emails_atualizada.append(texto)

my_set = set(list_emails_atualizada)
list_emails_norepeat = list(my_set)

list_emails.close()

resetSenha(list_emails_norepeat)