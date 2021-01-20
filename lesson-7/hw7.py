'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции 
сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой 
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.'''

from pandas import DataFrame
import numpy as np

class Matrix:
    
    def __init__(self, matrix: list):
        self.matrix = np.array(matrix)
        
    def __str__(self):
        return str(DataFrame(data = self.matrix, columns = ['' for i in range(len(self.matrix[0]))], index = ['' for i in range(len(self.matrix))]))
    
    def __add__(self, other):
        return Matrix((self.matrix + other.matrix).tolist())
    
'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. 
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_w(self):
        return self.width / 6.5 + 0.5

    def get_square_h(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_w = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_w}'


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_h = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_h}'


'''
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть 
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), 
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и 
выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. 
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, 
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек 
этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
Тогда метод make_order() вернет строку: *****\n*****\n**.Или, количество ячеек клетки равняется 15, количество 
ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
'''

class Cell:
    
    def __init__(self, num: int):
        self.age = num
        
    def __add__(self, other):
        return Cell(self.age + other.age)
        
    def __sub__(self, other):
        
        if self.age != other.age:
            return Cell(abs(self.age - other.age))
        else:
            print('Они поглотили друг друга')
            return False
        
    def __mul__(self, other):
        return Cell(int(self.age * other.age))
        
    def __truediv__(self, other):
        return Cell(round(self.age // other.age))
    
    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.age / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.age % cells_in_row)}'
        return row    