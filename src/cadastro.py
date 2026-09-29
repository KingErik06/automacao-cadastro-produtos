#Importações...
import pyautogui
import pandas as pd
from time import sleep

#Variáveis...
pyautogui.PAUSE = 1

#Lógica...
def cadastro(codigo, marca, tipo, categoria, preco_unitario, custo, obs):
    pyautogui.press('tab')
    pyautogui.write(codigo)
    pyautogui.press('tab')
    pyautogui.write(marca)
    pyautogui.press('tab')
    pyautogui.write(tipo)
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    for _ in range(16):
        pyautogui.press('tab')
