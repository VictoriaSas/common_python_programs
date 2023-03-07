"""
Скрипт с интерфейсом командной строки для вывода на экран записанных данных. Нумерация записей начинается с 1.
Логика:
просто запуск — вывод всех записей;
запуск с одним параметром-числом — вывод всех записей с номера, равного этому числу;
запуск с двумя числами — вывод записей, начиная с номера, равного первому числу, по номер, равный
второму числу, включительно.
"""
import sys


def main(argv):
    _, *args = argv

    if len(args) == 0:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            print(f.read())

    else:
        counter = 1
        i = False
        with open('bakery.csv', 'r', encoding='utf-8') as f:

            if len(args) == 1:
                for line in f:
                    if counter == int(args[0]):
                        i = True
                    if i is True:
                        print(line[:-1])
                    counter += 1

            if len(args) == 2:
                for line in f:
                    if counter == int(args[0]):
                        i = True
                    if i is True:
                        print(line[:-1])
                    if counter == int(args[1]):
                        i = False
                    counter += 1


if __name__ == '__main__':
    main(sys.argv)
