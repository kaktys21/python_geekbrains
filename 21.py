'''Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.'''

s = [1,'1',(1,),{1:'1'},{1},(i for i in range(5)), None]
for elem in s:
    print(f'{elem}\t\t{type(elem)}')