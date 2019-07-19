# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

print('-' * 50)
print('Задача - 1')
print('-' * 50)

class TownCar:
    def __init__(self, model, speed, color):
        self.name = model
        self.speed = speed
        self._color = color
        self._is_police = False

    def color(self):
        print(self.name + "'s color:", self._color)

    def is_police(self):
        if not self._is_police:
            print(self.name, 'is not a police car')
        else:
            print('Carefully!', self.name, 'is a police car')

    def go(self):
        print(self.name, 'started going.', 'Speed:', self.speed)

    def stop(self):
        print(self.name, 'stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')


class SportCar:
    def __init__(self, model, speed, color):
        self.name = model
        self.speed = speed
        self._color = color
        self._is_police = False

    def color(self):
        print(self.name + "'s color:", self._color)

    def is_police(self):
        if not self._is_police:
            print(self.name, 'is not a police car')
        else:
            print('Carefully!', self.name, 'is a police car')

    def go(self):
        print(self.name, 'started going.', 'Speed:', self.speed)

    def stop(self):
        print(self.name, 'stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')


class WorkCar:
    def __init__(self, model, speed, color):
        self.name = model
        self.speed = speed
        self._color = color
        self._is_police = False

    def color(self):
        print(self.name + "'s color:", self._color)

    def is_police(self):
        if not self._is_police:
            print(self.name, 'is not a police car')
        else:
            print('Carefully!', self.name, 'is a police car')

    def go(self):
        print(self.name, 'started going.', 'Speed:', self.speed)

    def stop(self):
        print(self.name, 'stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')


class PoliceCar:
    def __init__(self, model, speed, color):
        self.name = model
        self.speed = speed
        self._color = color
        self._is_police = True

    def color(self):
        print(self.name + "'s color:", self._color)

    def is_police(self):
        if not self._is_police:
            print(self.name, 'is not a police car')
        else:
            print('Carefully!', self.name, 'is a police car')

    def go(self):
        print(self.name, 'started going.', 'Speed:', self.speed)

    def stop(self):
        print(self.name, 'stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')


car_1 = TownCar('Volvo', 250, 'black')
car_2 = SportCar('Jaguar', 320, 'red')
car_3 = WorkCar('Ford', 170, 'yellow')
car_4 = PoliceCar('Mercedes', 300, 'white/blue')
print(car_1.name)
car_4.is_police()
car_3.is_police()
car_2.go()
car_4.color()
car_3.turn(input('Specify a turn direction: '))
car_1.stop()
car_2.color()


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class AllCars(TownCar, SportCar, WorkCar, PoliceCar):
    def __init__(self, model, speed, color, police):
        super().__init__(model, speed, color)
        self._is_police = police

car_5 = AllCars('Lada', 180, 'orange', True)
car_5.color()
car_5.go()
car_5.is_police()
car_5.stop()