'''Третья домашка GeekBrains python '''


'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

def Div(a, b):
    return a / b if b != 0 else False


'''2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.'''

def UserInfo(name, fname, byear, lcity, email, number):
    print('имя{:>20}\nфамилия{:>20}\nгод рождения{:>20}\nгород проживания{:>20}\nemail{:>20}\nтелефон{:>20}'.format(name, fname, byear, lcity, email, number))


'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''

def MaxSum(a, b, c):
    return sum(sorted([a, b, c])[:2])
    

'''4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.'''

def PowerRecurr(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / PowerRecurr(x, -n)
    if n % 2 == 0:
        return PowerRecurr(x, n // 2) * PowerRecurr(x, n // 2)
    else:
        return PowerRecurr(x, n - 1) * x    
 
    
def PowerBuiltin(x, n):
    return x ** n
 
 
def PowerFor(x, n):
    res = 1
    for i in range(-n):
        res *= 1 / x
    return res


'''5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''

def LineSum(summ = 0):
    line = input().split()
    for s in line:
        if s.isnumeric():
            summ += int(s)
        else:
            return summ
    return LineSum(summ)


'''6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.'''

def Capitalizer(word):
    return chr(ord(word[0]) - 32) + word[1:]


'''6.c Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().'''

def LineCapitalizer(line):
    return str(' '.join(Capitalizer(word) for word in line.split()))


''' Вызов функций '''

def Main():
    Div(int(input()), int(input()))
    UserInfo(name = 'Егор', fname = 'Епишев', byear = 1999, lcity = 'Москва', email = 'epishegor@yandex.ru', number = 88005553535)
    MaxSum(int(input()), int(input()), int(input()))
    PowerRecurr(float(input()), int(input()))
    PowerBuiltin(float(input()), int(input()))
    PowerFor(float(input()), int(input()))
    LineSum()
    Capitalizer(input())
    LineCapitalizer(input())
