﻿# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
print('-' * 40)
print('Задание - 1')
print('-' * 40)

def answer(name, age, city):
    info = f'{name}, {age} год(а), проживает в городе {city}'
    print(info)
answer(str.title(input('Введите имя: ')), input('Введите возраст: '), str.title(input('Введите город проживания: ')))
input()

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

print('-' * 40)
print('Задание - 2')
print('-' * 40)

def max_num(x, y, z):
    max_val = max(x, y, z, key=int)
    print('Максимальное число: ', max_val)
max_num(input('Введите 1-е число: '), input('Введите 2-е число: '), input('Введите 3-е число: '))
input()
# или
numbers = (input('Введите 1-е число: '), input('Введите 2-е число: '), input('Введите 3-е число: '))
def num(x):
     return int(x)
max_num = max(map(num, numbers))
print(max_num)
input()

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
print('-' * 40)
print('Задание - 3')
print('-' * 40)

fruits = ('яблоко', 'маракуйя', 'киви', 'персик', 'апельсин', 'банан', 'гранадилла', 'хурма')
max_len = max(map(lambda s: len(s), fruits))
print(max_len)

