"""
Редактирование данных.
При записи передавать из командной строки номер записи и новое значение.
При этом файл не должен читаться целиком — обязательное требование.
"""
import sys


def main(argv):
    _, num, changed_sale = argv
    num = int(num)

    with open('bakery.csv', 'r+', encoding='utf-8') as f1, open('for_overwriting.csv', 'w', encoding='utf-8') as f2:
        if num > 0 and num <= len(f1.readlines()):
            f1.seek(0)
            counter = 1
            for line in f1:
                if counter == num:
                    f2.writelines(f'{changed_sale}\n')
                else:
                    f2.write(line)
                counter += 1
        else:
            print('No such line')

    with open('bakery.csv', 'w', encoding='utf-8') as f1, open('for_overwriting.csv', 'r', encoding='utf-8') as f2:
        f1.write(f2.read())
    print('Ready')


if __name__ == '__main__':
    main(sys.argv)
