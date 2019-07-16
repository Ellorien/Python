import os
import shutil
import sys

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print('-' * 50)
print('Задача - 1')
print('-' * 50)

def mk_dir(dir_name):
    try:
        os.mkdir(dir_name)
        print(f'Создана директория {dir_name}')
    except FileExistsError:
        print(f'Директория {dir_name} уже существует')


for i in range(1, 10):
    mk_dir('dir_' + str(i))

input()

def del_dir(dir_name):
    try:
        os.rmdir(dir_name)
        print(f'Директория {dir_name} удалена')
    except FileNotFoundError:
        print(f'Директория {dir_name} не найдена')


for i in range(1, 10):
    del_dir('dir_' + str(i))

input()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('-' * 50)
print('Задача - 2')
print('-' * 50)

dir_list = [f for f in os.listdir() if os.path.isdir(f)]
print(dir_list)

input()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('-' * 50)
print('Задача - 3')
print('-' * 50)

shutil.copy(sys.argv[0], sys.argv[0] + '.copy')
file_list = [x for x in os.listdir() if os.path.isfile(x)]
print(file_list)

