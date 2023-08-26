import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def tempo_variado():
    tempo_espera = random.randint(5, 200)
    time.sleep(tempo_espera)

def comentar_post(usernamesList, url_post):
    navegador.get(url_post)
    time.sleep(4)

    for i, username in enumerate(usernamesList):

        # if i + 1 < len(usernamesList):
        #     next_username = usernamesList[i + 1]
        #     next_username2 = usernamesList[i + 2]
        # else:
        #     pass

        comentario = f'@{username}'

        navegador.find_element(By.CLASS_NAME, '_akhn').click()
        time.sleep(1)
        
        campo_comentario = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
        campo_comentario.send_keys(comentario)
        time.sleep(2)

        botao_comentar = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/div[2]/div')
        botao_comentar.click()

        print(comentario)
        print("Comentário realizado com sucesso!")
        tempo_variado()

def fazer_login(url_login, username, password):
    navegador.get(url_login)
    time.sleep(3)

    campo_usuario = navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    campo_usuario.send_keys(username)
    time.sleep(2)

    campo_senha = navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    campo_senha.send_keys(password)
    time.sleep(2)

    botao_entrar = navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
    botao_entrar.click()

    time.sleep(10)

    try:
        botao_notificacao = navegador.find_element(By.XPATH, '//*[@id="mount_0_0_KY"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]')
        time.sleep(3)
        botao_notificacao.click()
    except NoSuchElementException:
        pass

    print("LOGADO!")

############################## CONFIGURATIONS #########################################
username = "sibayal298"
password = "siba987654321"
url_login = 'https://www.instagram.com/accounts/login/'
url_post = 'https://www.instagram.com/p/CwWHcCWM2xs/'

usernamesList = open (r'E:\followers.txt', 'r', encoding='utf-8')
listUser_format = []

for user in usernamesList:
    listUser_format.append(user.strip())

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#######################################################################################
fazer_login(url_login, username, password)
comentar_post(listUser_format, url_post)

usernamesList.close()

print("Programa finalizado!")