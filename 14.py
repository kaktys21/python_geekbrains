'''Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.'''

num = input('Enter num: ')
maxNum = num[0]
i = 1
while i < len(num):
    if num[i] > maxNum:
        maxNum = num[i]
    i += 1
    
print(maxNum)