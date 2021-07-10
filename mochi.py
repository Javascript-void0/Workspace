import time, keyboard

time.sleep(5)
for i in range(0, 49):
    keyboard.press_and_release("v")
    time.sleep(0.005)
    keyboard.press_and_release("v")
    time.sleep(0.005)
    keyboard.press_and_release("left")
    time.sleep(0.1)

print('done')