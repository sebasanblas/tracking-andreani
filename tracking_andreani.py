#!/usr/bin/env python3

'''
Script para saber status de paquete de Andreani

Escrito por Sebastian San Blas.

2020.
'''

import os
import sys
import time
import logging
import socket
import telegram
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

def send(msg):

    '''Función para enviar mensaje a bot de telegram '''

    token = "XXX:YYY" # Colocar token de bot personal
    chat_id = "000000" # Colocar ID de chat

    bot = telegram.Bot(token=token)

    bot.sendMessage(chat_id=chat_id, text=msg)

def status_pack():

    '''Función para acceder a la pagina de Andreani y extraer status del envio'''

    options = Options()

    options.BinaryLocation = '/Applications/Chromium.app/Contents/MacOS/Chromium' #Cambiar ubicación de Chromium/Google Chrome si es necesario

    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    try:
        driver = webdriver.Chrome(executable_path=os.getcwd()+'/chromedriver',
                                  options=options)
        time.sleep(10)
        driver.get("https://usuarios.e-andreani.com/#!/informacionEnvio/XXXX") #Colocar numero de tracking provisto por Andreani en XXXX

        time.sleep(10)

        txt_1 = driver.find_element_by_class_name("center-items").text

        txt_2 = driver.find_element_by_class_name("collapse-content").text

        driver.quit()

        return txt_1, txt_2

    except WebDriverException as error_status:
        logging.basicConfig(filename=os.getcwd()+'/tracking_andreani.log',
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(error_status)
        send("Fallo abriendo WebDriver")
        send(error_status)

def internet(host="8.8.8.8", port=53, timeout=3):

    """
    Función que verifica el correcto funcionamiento de internet
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """

    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as error_internet:
        logging.basicConfig(filename=os.getcwd()+'/tracking_andreani.log',
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.error(error_internet)
        return False

os.chdir("xxxx") # Colocar ubicación de la carpeta contenedora. Ejemplo: "/Users/seba/Downloads/tracking-andreani/"

with open(os.path.join(sys.path[0], "diccionario_1.txt"), "r") as f_1:
    DIC_1 = f_1.read()
with open(os.path.join(sys.path[0], "diccionario_2.txt"), "r") as f_2:
    DIC_2 = f_2.read()

if internet() is True:

    TEXT_1, TEXT_2 = status_pack()

    if TEXT_1 != DIC_1 and TEXT_2 != DIC_2:

        try:
            send(TEXT_1)
            send(TEXT_2)
            with open(os.path.join(sys.path[0], "diccionario_1.txt"), "w") as f_1:
                f_1.write(str(TEXT_1))
                f_1.close()
            with open(os.path.join(sys.path[0], "diccionario_2.txt"), "w") as f_2:
                f_2.write(str(TEXT_2))
                f_2.close()

        except Exception as error_telegram_1:
            logging.basicConfig(filename=os.getcwd()+'/tracking_andreani.log',
                                format='%(name)s - %(levelname)s - %(message)s')
            logging.error(error_telegram_1)

    elif TEXT_1 == DIC_1 and TEXT_2 == DIC_2:
        try:
            print("Todo igual")
        except Exception as error_telegram_2:
            logging.basicConfig(filename=os.getcwd()+'/tracking_andreani.log',
                                format='%(name)s - %(levelname)s - %(message)s')
            logging.error(error_telegram_2)

    else:
        print("Error, algo fallo")
