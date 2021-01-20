'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить 
валидацию (проверку на корректность) числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''

from datetime import date
import traceback

class Date:
    
    def __init__(self, date):
        self.day, self.month, self.year = date.split('-')
    
    @classmethod
    def getter(cls, date):
        day, month, year = date.split('-')
        return {'day':int(day), 'month':int(month), 'year':int(year)}
    
    @staticmethod
    def lazy_validation(day, month, year):
        try:
            t = date(year, month, day)
            print('Correct date')
        except Exception as err:
            print(str(err).capitalize())        
    
    @staticmethod
    def visocos(year):     
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
    @staticmethod
    def norm_validation(day, month, year):
        month_day = {1: 30, 2: 29, 3: 30, 4: 31, 5: 30, 6: 31, 7: 30, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        month_name = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 
                      8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        
        v = Date.visocos(year)
        flag = True
        if 1 > day or day > 31:
            print('Day must be in 1...31')
            flag = False
            
        if 1 > month or month > 12:
            print('Month must be in 1...12')
            flag = False
            
        if (1 > month or month < 12) and day > month_day[month]:
            print(f'{month_name[month]} has maximum {month_day[month]} days')
            flag = False
        
        if month == 2 and v == False and day == 29:
            print(f'This year max 28 days in {month_name[2]}')
            flag = False
        
        if flag == True:
            print('Correct date')
            

'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''        
        
class ZeroDivision(Exception):
    
    def __init__(self, text):
        self.text = text

inp_data = input('a/b:\t').split('/')
try:
    if int(inp_data[1]) == 0:
        raise ZeroDivision("Zero division!")
except ZeroDivision as err:
    print(err)



'''3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, 
введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного элемента необходимо 
реализовать проверку типа элемента и вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст
(не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.'''        

class ListError(Exception):
    
    def __init__(self, text):
        self.text = text

corr_list = []
while True:
    nexter = 0
    try:
        adder = input('Next number:\t')
        try:
            adder = int(adder)
        except:
            raise ListError('Only numbers')
        corr_list.append(adder)
    except ListError as err:
        print(err)
        nexter = input('More?\nY\\N\t').lower()
    if nexter == 'n':
        print(corr_list)
        break

'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над прошлым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, нельзя отправить принтеры в виде строки или меньше 0.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.'''

class OfficeEquipmentStore:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Cost': self.price, 'Number': self.quantity}

    def __str__(self):
        return f'{self.name} cost {self.price} number {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Enter model:\t')
            unit_p = int(input(f'Enter cost:\t'))
            unit_q = int(input(f'Enter number:\t'))
            unique = {'Model': unit, 'Cost': unit_p, 'Number': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
        except:
            return f'Update error'

        print(f'Continue?\nY\\N')
        q = input(f'---> ').lower()
        if q == 'n':
            self.my_store_full.append(self.my_store)
            print(f'Final store:\n{self.my_store_full}')
            return f'Quit'
        else:
            return OfficeEquipmentStore.reception(self)
        
class Printer(OfficeEquipmentStore):
    
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(OfficeEquipmentStore):
    
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(OfficeEquipmentStore):
    
    def to_copier(self):
        return f'to copier smth {self.numb} times'
    
'''7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса 
(комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.'''


class ComplexNumber:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - (self.b * other.b), self.b * other.a)

    def __str__(self):
        return f'{self.a} + {self.b} * i'
    
def god_all_tester():
     
    #------1------
    today = Date('11 - 1 - 2001')
    print(today)
    Date.norm_validation(11, 11, 2022)
    today.norm_validation(11, 13, 2011)
    print(Date.getter('11-11-2011'))
    print(today.getter('11-11-2020'))
    Date.norm_validation(1, 11, 2000)
    
    #------2------
    div = ZeroDivision(10, 100)
    print(ZeroDivision.divide_by_null(10, 0))
    print(ZeroDivision.divide_by_null(10, 0.1))
    print(div.divide_by_null(100, 0)) 
    
    #------3------
    l = ListError(1)
    print(l.list_filler())   
    
    #-----4-6-----
    unit_1 = Printer('hp', 2000, 5, 10)
    unit_2 = Scanner('Canon', 1200, 5, 10)
    unit_3 = Copier('Xerox', 1500, 1, 15)
    print(unit_1.reception())
    print(unit_1.to_print())
    print(unit_3.to_copier())
    
    #------7------
    z_1 = ComplexNumber(1, -2)
    z_2 = ComplexNumber(3, 4)
    print(z_1)
    print(z_1 + z_2)
    print(z_1 * z_2)
    
god_all_tester()
