import os

filename = input('Input Filename: ')

with open(f'numin/{filename}.in', 'r') as fin, open(f'numin/{filename}.out', 'w') as fout:
    for line in fin:
        dict = dict(line.split(': '))
        split = line.split(' ', 1)

        fout.write(f'{split}' + '\n')
print('Done')

# Trash