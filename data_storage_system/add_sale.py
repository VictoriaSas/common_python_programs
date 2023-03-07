"""
Скрипт с интерфейсом командной строки для записи данных. Нумерация записей начинается с 1.
При записи передавать из командной строки значение суммы продаж.
Данные хранить в файле bakery.csv в кодировке utf-8.
"""
import sys


def main(argv):
    _, args = argv
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{args}\n')


if __name__ == '__main__':
    main(sys.argv)
