import os

def mk_dir(dir_name):
    try:
        os.mkdir(dir_name)
        print(f'Создана директория {dir_name}')
    except FileExistsError:
        print(f'Директория {dir_name} уже существует')


def del_dir(dir_name):
    try:
        os.rmdir(dir_name)
        print(f'Директория {dir_name} удалена')
    except FileNotFoundError:
        print(f'Директория {dir_name} не найдена')


def list_dir():
    for i in os.listdir():
        print(i)


def into_dir(dir_name):
    os.chdir(dir_name)
    print(os.getcwd())

