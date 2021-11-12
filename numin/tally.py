import keyboard

c = 0
x = 0

print('Started Counting')
while True:
    if keyboard.read_key() == 'x':
        x += 1
        print(x)
    if keyboard.read_key() == 'c':
        c += 1
        print(c)
    if keyboard.read_key() == 'z':
        break

total = c + x

print(f'Correct: {c} / {total}')
print(f'Incorrect: {x} / {total}')
print(f'{round((c / (c+x) * 100), 2)}% Correct')