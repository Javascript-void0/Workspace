import os


for root, dirs, files in os.walk('.\obsidian-move\slite', topdown=False):
    for name in files:
        if name[-3:] != '.md':
            print(name)
            os.remove(f'.\obsidian-move\slite\{name}')