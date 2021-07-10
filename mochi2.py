import keyboard
import time
print('Started')

# while True:
#     keyboard.wait('ctrl+enter')
#     time.sleep(0.1)
#     keyboard.write('''}}

# () 
# > 

# Synonym: 
# Antonym: ''')
#     keyboard.press_and_release('left')
#     time.sleep(0.1)
#     for i in range(6):
#         keyboard.press_and_release('up')
#     time.sleep(0.1)
#     keyboard.write('### {{')
#     print('Setup New Card')

while True:
    keyboard.wait('ctrl+enter')
    time.sleep(0.1)
    keyboard.write('''### {{}}

() 
> 

Synonym: 
Antonym: ''')
    time.sleep(0.1)
    for i in range(12):
        keyboard.press_and_release('left')
        keyboard.press_and_release('up')
    print('Setup New Card')