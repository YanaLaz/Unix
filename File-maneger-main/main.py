# coding=utf-8
import os
import shutil

"""
функция создание папки 
"""
def create_f(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Создать директорию %s не удалось" % path)
    else:
        print ("Успешно создана директория %s " % path)

"""
функция удаления папки
"""

def delete_f(path):
    try:
        shutil.rmtree(path)
    except OSError:
        print ("Удалить директорию %s не удалось" % path)
    else:
        print ("Успешно удалена директория %s " % path)


"""
функция перехода между директориями
"""
def cd_f(path):
    try:
        os.chdir(path)
    except OSError:
        print ("Перейти в директорию %s не удалось" % path)
    else:
        print ("Переход в директорию %s " % path)

"""
функция перехода наверх
"""
def cd_up(path):
    try:
        temp = path[:path.rfind("/")]
        os.chdir(temp)  # смена директории
    except OSError:
        print ("Перейти в директорию %s не удалось" % temp)
    else:
        print ("Переход в директорию %s " % temp)

"""
функция создания файла
"""
def touch_f(name):
    try:
        f = file(name, "w")
    except OSError:
        print ("Создать файл %s не удалось" % name)
    else:
        print ("Файл %s создан" % name)

"""
функция записи в файл
"""
def write_f(path, name):
    try:
        text = str(raw_input('Введите текст для записи: '))
        with open(path, "a+") as f:
            f.write("\n" + text)
    except OSError:
        print ("Не удалось добавить запись в %s" % name)
    else:
        print ("Запись в файл %s добавлена" % name)

"""
функция чтения  файла
"""
def read_f(path):
    try:
        f = open(path, "r")
        lines = f.read()
        print(lines)
    except Exception:
        print("Файла не существует.")

"""
функция удаления  файла
"""
def rm_f(path, name):
    try:
        os.remove(path)
        print("Удаление файла %s прошло успешно" % name)
    except Exception:
        print("Файл не найдены")



"""
функция копирования файла в папку
"""
def mv(path1, path):
    try:
        fold = str(raw_input('Введите в какую папку копировать: '))
        path_new = path1 + '/' + fold
        shutil.copy(path, path_new)
    except Exception:
        print ("Копировать файл в директорию %s не удалось" % path)
    else:
        print ("Файл успешно скопирован в директорию %s " % path)

"""
функция перемещения файла в папку
"""
def mv_f(path1, path):
    try:
        fold = str(raw_input('Введите в какую папку переместить: '))
        path_new = path1 + '/' + fold
        shutil.move(path, path_new)
    except Exception:
        print ("Переместить файл в директорию %s не удалось" % path)
    else:
        print ("Файл успешно перемещен в директорию %s " % path)


"""
функция переименования файла
"""
def rename(name):
    try:
        name_new = str(raw_input('Введите новое имя: '))
        os.rename(name, name_new)
    except Exception:
        print ("Файл %s не удалось переименовать" % name)
    else:
        print ("Файл %s успешно переименован" % name)



while True:
    try:
        print('\nПривет! \nЭто файловый менеджер \n\nДля работы укажите одну из цифр и имя: \n1 Имя - Создание папки \n2 Имя - Удаление папки \n3 Имя - Перейти в папку по имени \n4 - Выход на уровень вверх \n5 Имя - Создание пустого файла \n6 Имя - Запись текста в файл \n7 Имя - Просмотр содержимого файла \n8 Имя - Удаление файла \n9 Имя Папка - Копирование файла в другую папку \n10 Имя Папка - Перемещение файлов \n11 Имя_старое Имя_новое - Переименование файла \nНапишите 0 для выхода')
        path1 = os.getcwd()  # определяем текущий каталог
        x = int(input('Введите команду: '))
        if x in (1, 2, 3, 5, 6, 7, 8, 9, 10, 11):
            name = str(raw_input('Введите имя: '))
            path = path1 + '/' + name
        if x == 0:
            break
        elif x == 1:
            create_f(path)
        elif x == 2:
            delete_f(path)
        elif x == 3:
            cd_f(path)
        elif x == 5:
            touch_f(name)
        elif x == 6:
            write_f(path, name)
        elif x == 7:
            read_f(path)
        elif x == 8:
            rm_f(path, name)
        elif x == 4:
            cd_up(path1)
        elif x == 9:
            mv(path1, path)
        elif x == 10:
            mv_f(path1, path)
        elif x == 11:
            rename(name)
        elif x == 0:
            break
        else:
            print("Такой команды нет")
    except KeyboardInterrupt as e:
        break