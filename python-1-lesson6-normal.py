# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

class Hero(Person):
    def _get_damage(self, enemy):
        return self.damage / enemy.armor

    def go_attack(self, enemy):
        enemy.health = int(round(enemy.health - self._get_damage(enemy), 0))

class Enemy(Hero):
    pass

elf = Hero('Legolas', 250, 40, 1.2)
orc = Enemy('Orc', 330, 25, 1.4)

class Battle:
    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2

    def fighting(self):
        print('-' * 50)
        print(f'Бой начался!!! {self._player1.name} напал на {self._player2.name}а!!!')
        print('-' * 50)
        agressor = self._player1
        while self._player1.health > 0 and self._player2.health > 0:
            if agressor == self._player1:
                self._player1.go_attack(self._player2)
                print(f'{self._player2.name} был атакован. Остаток здоровья: ', self._player2.health)
                agressor = self._player2
            else:
                self._player2.go_attack(self._player1)
                print(f'{self._player1.name} получил отпор. Остаток здоровья: ', self._player1.health)
                agressor = self._player1
        print(f'{self._player1.name} выиграл бой!') if self._player1.health > 0 else print(
            f'{self._player2.name} победил!')

# battle = Battle(elf, orc)
battle = Battle(orc, elf)

battle.fighting()

