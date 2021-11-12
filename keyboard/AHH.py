import time, keyboard, sys
g = input("Enter word")
hmu = int(input("Enter how many times"))
wttime = int(input("How much time until execution?"))

time.sleep(wttime)
while hmu > 0:
    hmu -= 1
    keyboard.write(g)
    keyboard.press_and_release("Enter")
    time.sleep(0.3)
    if keyboard.is_pressed("Esc"):
        sys.exit()