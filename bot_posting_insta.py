import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def limpar_cookies():
    navegador.get('https://www.instagram.com/accounts/login/')
    navegador.delete_all_cookies()
    print("Cookies da sessão limpos com sucesso!")

def tempo_variado():
    tempo_espera = random.randint(3, 600)
    time.sleep(tempo_espera)

def comentar_post(usernamesList, url_post):
    navegador.get(url_post)

    for username in usernamesList:
        comentario = f'@{username}'

        campo_comentario = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
        campo_comentario.send_keys(comentario)

        botao_comentar = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]')
        botao_comentar.click()
        time.sleep(5)

        print(comentario)
        print("Comentário realizado com sucesso!")
        tempo_variado()
    navegador.quit()

def fazer_login(url_login, username, password):
    navegador.get(url_login)

    campo_usuario = navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    campo_usuario.send_keys(username)
    time.sleep(5)

    campo_senha = navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    campo_senha.send_keys(password)
    time.sleep(5)

    botao_entrar = navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
    botao_entrar.click()

    time.sleep(10)
    print("LOGADO!")

    if navegador.current_url == r'https://www.instagram.com/accounts/onetap/?next=%2F':
        info_login = navegador.find_element(By.XPATH, '//*[@id="mount_0_0_sF"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        info_login.click()
        time.sleep(5)

def obter_seguidores(perfil_alvo):
    navegador.get(f'https://www.instagram.com/{perfil_alvo}/')

    link_seguidores = navegador.find_element(By.XPATH, '//*[@id="mount_0_0_qS"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
    link_seguidores.click()
    time.sleep(5)

    seguidores_container = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

    #SCROLL PARA CARREGAR MAIS SEGUIDORES
    while True:
        navegador.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', seguidores_container)
        try:
            WebDriverWait(navegador, 8).until(lambda navegador: navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'))
        except:
            break

    #OBTÉM A LISTA DE SEGUIDORES
    seguidores_elems = navegador.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div')
    seguidores = []

    for seguidor in seguidores_elems:
        seguidores.append(seguidor.text)

    return seguidores

############################## CONFIGURATIONS #########################################
username = "sibayal298"
password = "siba987654321"
url_login = 'https://www.instagram.com/accounts/login/'
url_post = 'https://www.instagram.com/p/Cul6XWEsrOz/'

options = Options()
options.add_argument('window-size=1280x720')
#options.add_argument('--headless')

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

#######################################################################################
fazer_login(url_login, username, password)

#usernamesList = obter_seguidores(carmonadj_)

#comentar_post(usernamesList, url_post)