with open('mochi/links.txt', 'r') as file:
    lines = file.readlines()

with open('mochi/export.txt', 'w', encoding='utf-8') as fout:
    fout.write('''![Cat](https://i.imgur.com/CM1XFIY.gif) ~♥~
## New SAT Vocabulary Index
''')

    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    row10 = []    

    for i in range(len(lines)):
        if i % 10 == 0:
            row1.append(lines[i])
        elif i % 10 == 1:
            row2.append(lines[i])
        elif i % 10 == 2:
            row3.append(lines[i])
        elif i % 10 == 3:
            row4.append(lines[i])
        elif i % 10 == 4:
            row5.append(lines[i])
        elif i % 10 == 5:
            row6.append(lines[i])
        elif i % 10 == 6:
            row7.append(lines[i])
        elif i % 10 == 7:
            row8.append(lines[i])
        elif i % 10 == 8:
            row9.append(lines[i])
        elif i % 10 == 9:  
            row10.append(lines[i])

    def listFormat(list):
        for i in range(len(list)):
            unit = list[i].replace('\n', '')[-2:]
            list[i] = f"[Unit {unit}]({list[i]})".replace('\n', '')
            if i > 0:
                list[i] = '⠀⠀⠀⠀⠀⠀⠀' + list[i]
        return ''.join(list)

    row1 = listFormat(row1)
    row2 = listFormat(row2)
    row3 = listFormat(row3)
    row4 = listFormat(row4)
    row5 = listFormat(row5)
    row6 = listFormat(row6)
    row7 = listFormat(row7)
    row8 = listFormat(row8)
    row9 = listFormat(row9)
    row10 = listFormat(row10)
    rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]
    for i in range(len(rows)):
        fout.write(rows[i] + '\n')

print('Done')