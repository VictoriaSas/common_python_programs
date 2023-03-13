"""
Класс создания карты для лото.

Генератор:
* построчно выбирает 4 пропущенных мест;
* построчно по возрастанию выбирает уникальное случайное число в десятке под каждую позицию
(1 место - от 1 до 10, 2 место - от 11 до 20 и т.д.);
* по столбцам сортирует числа от меньшего (сверху) к большему (снизу)

Вывод строкой:
Выводит в формате карточки:
-----------------------------
  3    23    44       78 81
       30 39    55 65    87
  8 19       47    68    90
-----------------------------
"""

from random import randint, shuffle


class CardForLoto:
    def __init__(self):
        self._numbs_in_card = {0: [], 1: [], 2: []}
        self.generator()

    def generator(self):
        all_numbs = {
            0: [],  # first line
            1: [],  # second line
            2: []  # third line
        }
        number_of_spaces = {
            0: [],  # first column
            1: [],  # second column
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }

        for i in range(3):
            missing_number = [x for x in range(1, 9)]
            shuffle(missing_number)
            missing_number = missing_number[:4]

            for x in range(1, 10):
                if x not in missing_number:
                    gen_number = randint(x * 10 - 9, x * 10)
                    while gen_number in all_numbs[0] or gen_number in all_numbs[1]:
                        gen_number = randint(x * 10 - 9, x * 10)
                    all_numbs[i].append(gen_number)
                else:
                    all_numbs[i].append('  ')
                    number_of_spaces[x - 1].append(i)

        for i in range(9):
            if len(number_of_spaces[i]) == 1:
                list_of_numb = []
                for j in range(3):
                    if j not in number_of_spaces[i]:
                        list_of_numb.append(all_numbs[j][i])
                list_of_numb.sort()

                if 0 in number_of_spaces[i]:
                    all_numbs[1][i] = list_of_numb[0]
                    all_numbs[2][i] = list_of_numb[1]
                if 1 in number_of_spaces[i]:
                    all_numbs[0][i] = list_of_numb[0]
                    all_numbs[2][i] = list_of_numb[1]
                if 2 in number_of_spaces[i]:
                    all_numbs[0][i] = list_of_numb[0]
                    all_numbs[1][i] = list_of_numb[1]

            if len(number_of_spaces[i]) == 0:
                list_of_numb = []
                for j in range(3):
                    list_of_numb.append(all_numbs[j][i])
                list_of_numb.sort()
                for j in range(3):
                    all_numbs[j][i] = list_of_numb[j]

        for i in range(3):
            for j in range(9):
                self._numbs_in_card[i].append(all_numbs[i][j])

    @property
    def my_card(self):
        return self._numbs_in_card

    def __str__(self):
        str_all_numbs = ''
        for i in range(3):
            for numb in self._numbs_in_card[i]:
                if len(str(numb)) == 1:
                    str_all_numbs = f'{str_all_numbs}  {numb}'
                else:
                    str_all_numbs = f'{str_all_numbs} {numb}'
            str_all_numbs = f'{str_all_numbs} \n'

        return f'-----------------------------\n{str_all_numbs}-----------------------------\n'
