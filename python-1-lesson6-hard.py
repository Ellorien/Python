# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class SoftToy:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def material(self):
        print('Сырье поступило на производство')

    def assembling(self):
        print('Происходит пошив продукции')

    def painting(self):
        print('Осуществлена финальная окраска игрушек')

class Toy(SoftToy):
    pass

class Manufacturing(Toy):

    def _creation(self):
        self.material()
        self.assembling()
        self.painting()

    def final(self):
        self._creation()
        toy = Toy(self.name, self.color, self.type)
        print('Выпущена продукция:', toy.name, toy.color, toy.type)
        print('-' * 60)

gena = Manufacturing('Крокодил', 'зеленый', 'мультипликационный персонаж')

gena.final()


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Animal(Toy):
    pass

class Cartoon(Toy):
    pass

class Manufact1(Manufacturing):

    def final(self):
        self._creation()
        if self.type == 'мультипликационный персонаж':
            toy1 = Cartoon(self.name, self.color, self.type)
            print('Выпущена продукция типа "Мультяшки":', toy1.name, toy1.color)
            print('-' * 60)
        elif self.type == 'животное':
            toy2 = Animal(self.name, self.color, self.type)
            print('Выпущена продукция типа "Звери":', toy2.name, toy2.color)
            print('-' * 60)
        else:
            toy3 = Toy(self.name, self.color, self.type)
            print('Выпущена продукция нового типа:', toy3.name, toy3.color, toy3.type)
            print('-' * 60)

animal = Manufact1('Жираф', 'оранжевый', 'животное')

animal.final()

cartoon = Manufact1('Стич', 'синий', 'мультипликационный персонаж')

cartoon.final()

some_toy = Manufact1('Молоток', 'красный', 'инструмент')

some_toy.final()