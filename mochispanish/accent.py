# coding: utf-8

file = open('./mochispanish/1a.txt', 'r')
lines = file.readline()
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

rewrite = open('./mochispanish/1a.txt', 'w')
rewrite.writelines(newlines)
rewrite.close()
print('done')

# no doesn't work