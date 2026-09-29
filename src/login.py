#Importando...
import pyautogui
from time import sleep

#Variáveis...
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "testedeautomacao@gmail.com"
senha = "testedeautomacao"
pyautogui.PAUSE = 3

#Lógica Principal...
def login():
    pyautogui.press('win')
    pyautogui.write('Microsoft Edge')
    sleep(2)
    pyautogui.press('enter')
    pyautogui.write(link)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('tab')
    pyautogui.write(email)
    pyautogui.press('tab')
    pyautogui.write(senha)
    pyautogui.press('tab')
    pyautogui.press('enter')