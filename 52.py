'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке'''

with open('TestText.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()

for lineNum in range(len(lines)):
    print(f'{lineNum + 1}:\t{len(lines[lineNum].split())}')