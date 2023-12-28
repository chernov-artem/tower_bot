import pyautogui as pag
import time
import cv2
import numpy as np

def find_coordinates(tmp: str) -> tuple:
    'функция поиска шаблона на изображении. Возвращает координаты'
    # Преобразование изображения в оттенки серого
    time.sleep(0.3)
    pag.screenshot('screenshot.png')
    time.sleep(0.3)
    template = cv2.imread(tmp, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread('screenshot.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск совпадения
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(result >= threshold)

    for pt in zip(*loc[::-1]):
        return pt

def osl():
    return find_coordinates('images/osl.png')

def gates():
    return find_coordinates('images/gates.png')

def avta():
    return find_coordinates('images/avta.png')

def find_n():
    return find_coordinates('images/n.png')

def find_cave():
    return find_coordinates('images/cave.png')

def tower_entrance():
    return find_coordinates('images/tower_entrance.png')

def enter_btn():
    return find_coordinates('images/enter.png')

def blue_cross_btn():
    return find_coordinates('images/blue_cross.png')