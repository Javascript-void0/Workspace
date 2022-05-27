import os
from os.path import exists

root = '.\obsidian-move\slite'
for root, dirs, files in os.walk(root, topdown=False):
    for name in files:
        if exists(f'.\obsidian-move\slite\{name}') == False:
            os.rename(f'{root}\{name}', f'.\obsidian-move\slite\{name}')
        else:
            print(f'{root}\{name}')