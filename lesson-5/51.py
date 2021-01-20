'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.'''

with open('FirstOuntPut.txt', 'w', encoding = 'utf-8') as output:
    while True:
        n = input()
        if n == '':
            break
        output.write(n + '\n')
        