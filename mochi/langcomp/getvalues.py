# reads existing lang/comp mochi deck to get values

file = open('./mochi/langcomp/get.json', 'r')
output = open('./mochi/langcomp/langcomp.txt', 'w')
lines = file.readlines()

for i in range(len(lines)-1, -1, -1):
    if 'value' in str(lines[i]):
        lines[i] = lines[i][44:]
        lines[i] = lines[i].replace('"', '| ')
    else:
        del lines[i]

for i in range(len(lines)):
    if (i + 1) % 4 != 0:
        lines[i] = lines[i].replace('\n', '')
    else:
        lines[i] = lines[i].replace('| ', '')

output.writelines(lines)
print('done')