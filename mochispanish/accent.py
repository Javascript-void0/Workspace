# coding: utf-8
filename = input('Enter a file name: ')
file = open(f'./mochispanish/list/{filename}.txt', 'r')
lines = file.readlines()
print(lines)
newlines = []
for line in lines:
    line = line.replace('á', 'a')
    line = line.replace('é', 'e')
    line = line.replace('í', 'i')
    line = line.replace('ó', 'o')
    line = line.replace('ú', 'u')
    line = line.replace('ñ', 'n')
    newlines.append(line)
    print(line)

rewrite = open('./mochispanish/list/1a.txt', 'w')
rewrite.writelines(newlines)
rewrite.close()
print('done')

# no doesn't work