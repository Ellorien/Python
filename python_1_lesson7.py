"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random

class LotoCard:
    def __init__(self, card_name):
        self.card_name = card_name
        self._lines = 3
        self._numbers = 5
        self._cells = 9
        self._place = list()

    def init(self, list):
        self._place = ['  ' for c in range(0, self._lines * self._cells)]
        for line in range(0, self._lines):
            start = line * 5
            nums = list[start:start + 5]
            nums.sort()
            for i in range(0, 5):
                start = line * self._cells
                cell = start + i * 2 + random.randint(0, 1)
                if cell >= start + self._cells:
                    cell = start + self._cells - 1
                self._place[cell] = nums[i]

    def _set_line(self, line, list):
        list.sort()
        current = -1
        for value in list:
            current = random.randint(current + 1, 10)
            self._place[9 * line + current] = value

    def search_num(self, num):
        try:
            self._place.index(num)
            return True
        except ValueError:
            return False

    def accepting(self, num):
        try:
            i = self._place.index(num)
            self._place[i] = '-'
            return True
        except ValueError:
            return False

    def card(self):
        print('-' * 44)
        print(f'Карточка {self.card_name}:')
        for line in range(0, self._lines):
            start = line * self._cells
            print(self._place[start:start + self._cells])
        print('-' * 44)


class GameLoto:
    def __init__(self):
        self.nums = []
        self.card_user = LotoCard('Player')
        self.card_comp = LotoCard('PC')

    def _init(self):
        self.nums = [i for i in range(1, 91)]
        self.card_init(self.card_user)
        self.card_init(self.card_comp)
        self.nums = [i for i in range(1, 91)]

    def _randnum(self):
        indx = random.randint(0, len(self.nums) - 1)
        return self.nums.pop(indx)

    def card_init(self, card):
        numbers = list()
        for i in range(0, 15):
            numbers.append(self._randnum())
        card.init(numbers)

    def start(self):
        while True:
            self._init()
            choice = input('Начать новую игру? (y/n)')
            if choice.lower() != 'y':
                return
            while len(self.nums) > 0:
                self.card_user.card()
                self.card_comp.card()
                num = self._randnum()
                print(f'\nНовый бочонок: {num} (осталось {len(self.nums)})')
                choice = input('Зачеркнуть цифру? (y/n)')

                choice1 = self.card_user.accepting(num)
                choice2 = self.card_comp.accepting(num)
                if choice.lower() == 'y':
                    if choice1 or choice2:
                        continue
                    print('\nЦифра отсутствуе. Игра закончена. Вы проиграли.')
                    return
                else:
                    if choice1 or choice2:
                        print('\nЦифра присуствует. Игра закончена. Вы проиграли.')
                        return

            if len(self.nums) == 0:
                print('\nВы Выиграли.')


loto = GameLoto()
loto.start()

