import sys
from time import sleep
from random import randint
from termcolor import colored

row_1 = ['   ', '|', '   ', '|', '   ', '\n']
row_2 = ['---', '+', '---', '+', '---', '\n']
row_3 = ['   ', '|', '   ', '|', '   ', '\n']
row_4 = ['---', '+', '---', '+', '---', '\n']
row_5 = ['   ', '|', '   ', '|', '   ', '\n']
board = [row_1, row_2, row_3, row_4, row_5]

def drawBoard():
    print(colored('\nTic', 'cyan') + colored('-Tac-', 'blue') + colored('Toe\n', 'cyan'))
    for column in board:
        for row in column:
            print(f'{row}', end='')
    print(' ')

def checkPosition(pos):
    if pos > 0 and pos < 10:
        if pos == 1 and row_1[0] == '   ':
            return True
        elif pos == 2 and row_1[2] == '   ':
            return True
        elif pos == 3 and row_1[4] == '   ':
            return True
        elif pos == 4 and row_3[0] == '   ':
            return True
        elif pos == 5 and row_3[2] == '   ':
            return True
        elif pos == 6 and row_3[4] == '   ':
            return True
        elif pos == 7 and row_5[0] == '   ':
            return True
        elif pos == 8 and row_5[2] == '   ':
            return True
        elif pos == 9 and row_5[4] == '   ':
            return True
    return False

def changeTile(pos, player):
    if player == 'user':
        mark = colored('X', 'yellow')
    elif player == 'cpu':
        mark = 'O'
    if pos == 1:
        row_1[0] = f' {mark} '
    elif pos == 2:
        row_1[2] = f' {mark} '
    elif pos == 3:
        row_1[4] = f' {mark} '
    elif pos == 4:
        row_3[0] = f' {mark} '
    elif pos == 5:
        row_3[2] = f' {mark} '
    elif pos == 6:
        row_3[4] = f' {mark} '
    elif pos == 7:
        row_5[0] = f' {mark} '
    elif pos == 8:
        row_5[2] = f' {mark} '
    elif pos == 9:
        row_5[4] = f' {mark} '

def cpuAnimation():
    sys.stdout.write('.     /\r')
    sys.stdout.flush()
    sleep(0.5)
    sys.stdout.write('..    |\r')
    sys.stdout.flush()
    sleep(0.5)
    sys.stdout.write('...   \\\r')
    sys.stdout.flush()
    sleep(0.5)
    sys.stdout.write('....  /\r')
    sys.stdout.flush()
    sleep(0.5)
    sys.stdout.write('..... |\r')
    sys.stdout.flush()
    sleep(0.5)
    sys.stdout.write('..... \\\r')
    sys.stdout.flush()
    sleep(0.5)
    sys.stdout.write('         ')
    sys.stdout.flush()

def winCheck(player):
    if player == 'user':
        mark = colored('X', 'yellow')
    elif player == 'cpu':
        mark = 'O'
    if row_1[0] == f' {mark} ' and row_1[2] == f' {mark} ' and row_1[4] == f' {mark} ':
        return True
    elif row_3[0] == f' {mark} ' and row_3[2] == f' {mark} ' and row_3[4] == f' {mark} ':
        return True
    elif row_5[0] == f' {mark} ' and row_5[2] == f' {mark} ' and row_5[4] == f' {mark} ':
        return True
    elif row_1[0] == f' {mark} ' and row_3[0] == f' {mark} ' and row_5[0] == f' {mark} ':
        return True
    elif row_1[2] == f' {mark} ' and row_3[2] == f' {mark} ' and row_5[2] == f' {mark} ':
        return True
    elif row_1[4] == f' {mark} ' and row_3[4] == f' {mark} ' and row_5[4] == f' {mark} ':
        return True
    elif row_1[0] == f' {mark} ' and row_3[2] == f' {mark} ' and row_5[4] == f' {mark} ':
        return True
    elif row_1[4] == f' {mark} ' and row_3[2] == f' {mark} ' and row_5[0] == f' {mark} ':
        return True
    return False

def fullBoardCheck():
    for i in range(5):
        if row_1[i] == '   ':
            return False
        if row_3[i] == '   ':
            return False
        if row_5[i] == '   ':
            return False
    return True

valid = False
while True:
    drawBoard()
    try:
        pos = int(input('Enter a position (1-9): '))
    except ValueError:
        pass
    try:
        if pos > 0 and pos < 10:
            if checkPosition(pos):
                changeTile(pos, 'user')
                print(' ')
                drawBoard()
                if winCheck('user'):
                    print(colored('  You Won!', 'green'))
                    break
                valid = True
            else:
                valid = False
        else:
            valid = False
    except NameError:
        pass
    if fullBoardCheck():
        print(colored('   Tie!', 'magenta'))
        break
    if valid:
        cpu_pos = randint(1, 9)
        while not checkPosition(cpu_pos):
            cpu_pos = randint(1, 9)   
        #cpuAnimation()
        changeTile(cpu_pos, 'cpu')
        print(' ')
        drawBoard()
        if winCheck('cpu'):
            print(colored(' You Lost!', 'red'))
            break