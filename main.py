import time

import functions
import images

def begin():
    functions.blue_cross()
    functions.forward()
    functions.gates()

if __name__ == '__main__':
    time.sleep(2)
    # functions.go_to_tower()
    # begin()
    # functions.gates()
    functions.from_floor_to_floor()
