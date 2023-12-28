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

def move_and_double_clic(x: int, y: int):
    mouse.move(x, y, 0.2)
    time.sleep(0.7)
    pag.doubleClick()
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

def go_to_tower():
    "функция захода в башню"
    xy_tmp = images.find_cave()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1000, 500)
    xy_tmp = images.tower_entrance()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1000, 500)
    xy_tmp = images.enter_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1000, 500)
    time.sleep(0.5)

def blue_cross():
    "функция нажатия на кнопку закрытия окна бафа"
    print('avta')
    xy_tmp = images.blue_cross_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 2, y + 3)
    else:
        pass
    time.sleep(0.5)

def avta():
    "функция нажатия на кнопку автобоя"
    print('avta')
    xy_tmp = images.avta()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1000, 500)
    time.sleep(0.5)

def find_n():
    "функция нажатия на N"
    xy_tmp = images.find_n()
    print(xy_tmp)
    # if xy_tmp != None:
    #     x, y = xy_tmp[0], xy_tmp[1]
    #     print(x, y)
    #     move_and_clic(x + 24, y + 8)
    # else:
    #     move_and_clic(1000, 500)
    # time.sleep(0.5)

def gates():
    "функция нажатия на ворота"
    # xy_tmp = images.gates()
    # if xy_tmp != None:
    #     x, y = xy_tmp[0], xy_tmp[1]
    #     print(x, y)
    #     move_and_clic(x + 24, y + 8)
    #     mouse.click('left')
    #     mouse.click('left')
    #     mouse.click('left')
    #
    # else:
    #     move_and_clic(1000, 400)
    #     move_and_clic(1000, 400)
    time.sleep(1)
    move_and_right_clic(839, 639)

def forward():
    print('forward')
    time.sleep(7)
    move_and_double_clic(936, 412)
    time.sleep(3)

def find_north():
    pag.hotkey('right')
    time.sleep(0.5)
    pag.hotkey('right')

def from_floor_to_floor(time_sec: int):
    blue_cross()
    forward()
    blue_cross()
    avta()
    time.sleep(time_sec)

# time.sleep(2)

# print('go')
# from_floor_to_floor()

# forward()
# gates()
# avta()
# while True:
#     n = images.find_n()
#     if n != None:
#         break
#     find_north()

# 1 этаж - 25-30 секунд
# 2 этаж - 40 секунд
# 3 этаж - 45 секунд
# 4 этаж - 48-50 секунд
# 5 этаж - секунд
# 6 этаж - секунд
# 7 этаж - 70 секунд