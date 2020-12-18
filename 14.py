'''Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.'''

'''через строки'''
num = input('Enter num: ')
maxNum = num[0]
i = 1
while i < len(num):
    if num[i] > maxNum:
        maxNum = num[i]
    i += 1
    
print(maxNum)

'''арифметика'''
num = int(input('Enter num: '))
maxNum = -1
while num != 0:
    CurNum = num % 10
    num //= 10
    if CurNum > maxNum:
        maxNum = CurNum
print(maxNum)
