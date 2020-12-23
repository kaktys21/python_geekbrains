'''Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().'''

s = [i for i in input('Enter line of numbers (sep = " "): ').split()]

for i in range(1, len(s), 2):
    s[i - 1], s[i] = s[i], s[i - 1]
    
print(s)