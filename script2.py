from time import sleep
import pyautogui
c = 1
x = 2
while x > c:
    pyautogui.press('win')
    sleep(1)
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.write('https://instagram.com/')
    pyautogui.press('enter')
    sleep(5)
    pyautogui.click(105, 259, duration=1.5)
    pyautogui.typewrite('thenotoriousmma')
    sleep(1)
    pyautogui.click(215, 266, duration=0.4)
    sleep(5)
    pyautogui.click(800, 578, duration=1)
    sleep(2)

    # Tentativa de localizar a imagem coracao.png
    try:
        coracao = pyautogui.locateCenterOnScreen('coracao.png')
        if coracao is None:
            print('Imagem "coracao.png" não encontrada.')


        else:
            print('Coordenadas do coração:', coracao, '... Fechando a Aba do instagram')
            pyautogui.hotkey('ctrl', 'w')
            sleep(86400)

            
    except pyautogui.ImageNotFoundException:
        print('Imagem "coracao.png" não encontrada.')
        pyautogui.click(1181, 884, duration=2)
        comentario = pyautogui.locateCenterOnScreen('comentario.png')
        sleep(3)
        pyautogui.click(comentario, duration= 1)
        pyautogui.typewrite('LETS GO!!')
        sleep(0.8)
        pyautogui.press('enter')
        sleep(3)
        pyautogui.hotkey('ctrl', 'w')
        sleep(86400)