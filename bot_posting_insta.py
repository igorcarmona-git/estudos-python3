import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

def random_time():
    waitTime = random.randint(3, 10)
    time.sleep(waitTime)

def randomTime_large():
    largeTime = random.randint(120, 600)
    time.sleep(largeTime)

def toComment_post(usernamesList, url_post):
    browser.get(url_post)
    time.sleep(4)

    for i, username in enumerate(usernamesList):
        if (i + 1) % 15 == 0:                           #verifica se i é multiplo de 20, nao precisa por varios or or or individual
            randomTime_large()
            print(f'\nA large time has been activated!\n')

        try:
            comment = f'@{username}'

            browser.find_element(By.CLASS_NAME, '_akhn').click()
            time.sleep(2)
            
            inputComment = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
            inputComment.send_keys(comment)
            time.sleep(2)

            buttonComment = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/div[2]/div')
            buttonComment.click()

            print(f'\n{i}) {comment}')
            print(f'The comment has been put!\n')

            random_time()
        except:
            continue

def do_login(url_login, username, password):
    browser.get(url_login)
    time.sleep(3)

    inputUser = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    inputUser.send_keys(username)
    time.sleep(2)

    inputPassword = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    inputPassword.send_keys(password)
    time.sleep(2)

    joinButton = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
    joinButton.click()

    time.sleep(10)

    try:
        notificationButton = browser.find_element(By.XPATH, '//*[@id="mount_0_0_KY"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]')
        time.sleep(3)
        notificationButton.click()
    except NoSuchElementException:
        pass

    print(f'\nLoggin succesfull!\n')

############################## CONFIGURATIONS #########################################
username = "sibayal298"
password = "siba987654321"
url_login = 'https://www.instagram.com/accounts/login/'
url_post = 'https://www.instagram.com/p/CyQtX4ZgNeJ/'

usernamesList = open (r'E:\followers.txt', 'r', encoding='utf-8')
listUser_format = []

for user in usernamesList:
    listUser_format.append(user.strip()) # strip --> Corta os espaços do começo e do fim da string
random.shuffle(listUser_format) #lista com posições desordenada da original

serviceDriver = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=serviceDriver)

################################# MAIN FLOW ######################################################
do_login(url_login, username, password)
toComment_post(listUser_format, url_post)

usernamesList.close()

print(f'\nSoftware has been closed, thank you!\n')