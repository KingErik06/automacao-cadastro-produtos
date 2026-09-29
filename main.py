#Importando...
import pyautogui

#Variáveis...
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "testedeautomacao@gmail.com"
senha = "testedeautomacao"
pyautogui.PAUSE = 2

#Lógica Principal...
pyautogui.press('win')
pyautogui.write('Opera GX')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
pyautogui.click(x=745, y=392)
pyautogui.write(email)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('tab')
pyautogui.press('enter')