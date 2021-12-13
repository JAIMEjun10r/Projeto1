import pyautogui as pg
from time import sleep
def arquitetura_de_computadores():
    pg.PAUSE = 1
    pg.press('winleft')
    pg.write('Chrome')
    pg.press('enter')
    sleep(1)
    pg.write('https://aulas.descomplica.com.br/graduacao/bacharelado-em-sistemas-de-informacao/')
    pg.press('enter')
    sleep(3)
    # aqui vou para abrir o office
    pg.moveTo(712, 744)
    sleep(0.2)
    pg.click()
    sleep(19.5)
    pg.moveTo(407, 356)
    sleep(0.2)
    pg.click()
    sleep(0.2)
    pg.moveTo(585, 294)
    pg.sleep(0.1)
    pg.click()
    sleep(4)
    # aqui terminei a parte do office
    pg.moveTo(118, 18)
    sleep(0.5)
    pg.click()
    sleep(0.4)
    pg.moveTo(42, 280)
    sleep(0.2)
    pg.click()
    sleep(5)
    # até aqui para chegar no menu das disciplinas
    pg.moveTo(437, 356)
    pg.click()
    sleep(0.6)
    pg.scroll(-492)
    sleep(0.7)
    pg.click()
    # aqui já estou dentro da disciplina de AC



