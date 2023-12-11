import keyboard
import mouse
import time
import images
import pyautogui as pag
# keyboard.write('Hello!', 0.1)



# mouse.move(419, 1052, 0.2)
# mouse.click('left')
# time.sleep(2)
# mouse.move(877, 976, 0.2)
# time.sleep(2)
# mouse.click('left')

def get_position():
    time.sleep(2)
    current_cursor = mouse.get_position()
    print(current_cursor)

def move_and_clic(x: int, y: int):
    mouse.move(x, y, 0.2)
    time.sleep(0.7)
    mouse.click('left')
    time.sleep(0.7)

def move_and_right_clic(x: int, y: int):
    mouse.move(x, y, 0.2)
    time.sleep(0.7)
    mouse.click('right')
    time.sleep(0.7)

def osl():
    "функция нажатия на осла"
    xy_tmp = images.osl()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1000, 500)
    time.sleep(0.5)

def gates():
    "функция нажатия на ворота"
    xy_tmp = images.gates()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
        mouse.click('left')

    else:
        move_and_clic(1000, 400)
        move_and_clic(1000, 400)
    time.sleep(1)
    move_and_clic(1000, 400)

time.sleep(2)
# gates()
mouse.click('left')
mouse.click('left')
pag.hotkey('ctrl', 'a')
