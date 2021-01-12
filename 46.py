'''6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.'''

from itertools import count, cycle

  
def a(n: int):
    return count(n)
    
def b(l: list):
    return cycle(l)

def tester():
    num = int(input())
    for i in a(num):
        print(i, end = '  ')
        if i == num * 10:
            break
    print()
    l = input().split()
    loops = 0
    for i in b(l):
        if i == l[-1]:
            loops += 1
        if loops == 4:
            print(i, end = ' ')
            break
        print(i, end = ' ')
        
tester()
