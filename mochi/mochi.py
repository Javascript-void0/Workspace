import sys
import time

import keyboard

count = 6
for i in range(6):
    time.sleep(1)
    count -= 1
    sys.stdout.write('\rStarting... ' + f'{count}')
sys.stdout.write('\rDo Not Move    ')
print('\r')

# ==== SINGLE DECK ====
for i in range(48):
    keyboard.press_and_release("v")
    time.sleep(0.005)
    keyboard.press_and_release("v")
    time.sleep(0.005)
    keyboard.press_and_release("left")
    time.sleep(0.1)
    if i < 9:
        sys.stdout.write(f'\r0{i+1}/48')
    else:
        sys.stdout.write(f'\r{i+1}/48')
print('\r')
print('Done :3')

# ==== INFINITE ====
# time.sleep(5)
# count = 0
# while True:
#     keyboard.press_and_release("v")
#     time.sleep(0.005)
#     keyboard.press_and_release("v")
#     time.sleep(0.005)
#     keyboard.press_and_release("left")
#     time.sleep(0.1)
#     count += 1
#     sys.stdout.write(f'\rcount')
