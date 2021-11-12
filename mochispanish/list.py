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

file = open('./mochispanish/1a.txt')
lines = file.readlines()
for line in lines:
    split = line.split('; ')
    spanish, english = split[0], split[1]
    print(spanish, english)
    t = 0.1
    keyboard.press_and_release("n")
    time.sleep(t)
    keyboard.write(english)
    time.sleep(t)
    keyboard.press_and_release("tab")
    time.sleep(t)
    keyboard.write(spanish)
    time.sleep(t)
    keyboard.press_and_release("ctrl+enter")
    time.sleep(t)
    keyboard.press_and_release("escape")
    time.sleep(t)
