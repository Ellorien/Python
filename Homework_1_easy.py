# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран
print('Задача-1')
# Простой вывод переменных неинтересен, поэтому выводил только результаты вычислений
c = 'Привет!'
d = 'Добро пожаловать в мир Python!!!'
print(c, d)
input()
a = 5
b = 9
print(a * b)
print(a ** b)
print(b / a)
print(b // a)
print(b % a)
input()
p = 3.14159265358979
print(a * p)
input()
radius = int(input('Введите радиус круга (в метрах): '))
circle_len = int(100 * 2 * p * radius) / 100
circle_area = int(100 * p * radius ** 2) / 100
print('Длина окружности: ' + str(circle_len) + ' м')
print('Площадь круга: ' + str(circle_area) + ' м')
input()

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
print('Задача-2')
number = int(input('Введите число: '))
print(number + 2)
input()

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
print('Задача-3')
age = int(input('Укажите Ваш возраст: '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')
