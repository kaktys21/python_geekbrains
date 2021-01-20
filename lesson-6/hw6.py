import time

'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.'''

class TrafficLight:
    
    def __init__(self):
        self.__color = 'красный'
        
    def running(self):
        colors = ['красный', 'желтый', 'зеленый']
        while True:
            self.__color = colors[0]
            time.sleep(7)
            self.__color = colors[1]
            time.sleep(2)
            self.__color = colors[2]
            time.sleep(10)
            
'''2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.'''

class Road:
    
    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width
        
    def mass(self):
        return str(round((self._length * self._width * 25 * 5) / 1000, 3)) + ' т'
    
'''3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''

class Worker:
    
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        
class Position(Worker):
    
    def get_full_name(self):
        return self.name + ' ' + self.surname
    
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
    
'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.'''

class Car:
    
    def __init__(self, speed, color, name, is_police = False):
        
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
        self.__is_running = False
        
    def go(self):
        
        if self.__is_running == False:
            print(f'{self.name} is running')
            self.__is_running = True
        else:
            print(f'{self.name} is already runnung')
            
    def stop(self):
        
        if self.__is_running == False:
            print(f'{self.name} is not running')
        else:
            print(f'{self.name} is stopped')        
            self.__is_runnung = False
        
    def turn(self, direction):
        print(f'{self.name} turned {direction}')
        
    def show_speed(self):
        print(f'{self.name} speed - {self.speed}')
        
class TownCar(Car):
    
    def show_speed(self):
        print(f'{self.name} speed - {self.speed}')
        
        if self.speed > 60:
            print('Slower down you speed racer!')
            
class WorkCar(Car):
    
    def show_speed(self):
        print(f'{self.name} speed - {self.speed}')
        
        if self.speed > 40:
            print('Slower down you speed racer!')
            
class SportCar(Car):
    
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name)
        
class PoliceCar(Car):
    
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
        print('I\'m the law!')
        
'''5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

class Stationery:
    
    def __init__(self, title):
        self.title = title
        
    def draw(self):
        print('Start  drawing')
        
class Pen(Stationery):
    
    def draw(self):
        print(f'Start drawing with pen named {self.title}')
        
class Pencil(Stationery):
    
    def draw(self):
        print(f'Start drawing with pencil named {self.title}')
        
class Handle(Stationery):
    
    def draw(self):
        print(f'Start drawing with handle named {self.title}')
        

def god_all_tester():
    
    #-------1-------
    light = TrafficLight()
    #light.running()
    
    #-------2-------
    road = Road(20, 2000)
    print(road.mass())
    
    #-------3-------
    stas = Position('Stas', 'Noname', 'God', 10000, 5000000)
    print(f'{stas.get_full_name()}\t{stas.get_total_income()}')
    
    #-------4-------
    audi = SportCar(100, 'Red', 'Audi')
    oka = TownCar(30, 'White', 'Oka')
    lada = WorkCar(70, 'Rose', 'Lada')
    ford = PoliceCar(110, 'Blue',  'Ford')
    print(audi.color)
    ford.stop()
    lada.turn('left')
    
    #-------5-------
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()
    pencil.draw()
    handle.draw()  

god_all_tester()