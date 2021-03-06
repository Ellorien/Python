﻿# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
print('-' * 40)
print('Задание - 1')
print('-' * 40)
names = ['Alexandr', 'Boris', 'Charles', 'Denis', 'Egor', 'Fedor', 'Gennady']
salary = [200000, 420000, 340000, 800000, 190000, 250000, 510000]
payroll = dict(zip(names, salary))

with open('salary.txt', 'w', encoding='utf-8') as file:
    for key, value in payroll.items():
        string = f'{key} - {value}\n'
        file.write(string.rjust((len(max(payroll, key=len))) + (len(str(max(payroll)))) + 3))

with open('salary.txt', 'r', encoding='utf-8') as file:
    for line in file:
        new = line.split()
        if int(new[2]) > 500000:
            continue
        print(str.upper(new[0]), new[1], int(int(new[2]) * 0.87))




