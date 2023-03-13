"""
Функции игры в Лото.

choose_number
Вход - числа от 1 до 90 включительно в случайном порядке, индекс последовательности, на котором остановились.
Вывод - число для хода, новый индекс последовательности.
Выбирает число из последовательности по индексу для каждого хода игры.

check_answer
Вход - игрок типа Person, ответ игрока как ход, число от 1 до 90 включительно в случайном порядке
Вывод - результат проверки (True/False)
Проверяет ход игрока, формат ввода.


play
Вход - игрок типа Person, компьютер типа Computer.
Вывод отсутствует
Непосредственно действия игры.
"""

from random import shuffle


def choose_number(all_numbers, count_for_numbs):
    if all_numbers is not None:
        final_numb = all_numbers[count_for_numbs]
        count_for_numbs += 1
        return final_numb, count_for_numbs
    else:
        return None, count_for_numbs


def check_answer(person, answer_person, number):
    pass
    flag = False
    is_right = False
    for i in range(3):
        if number in person.players_card.my_card[i]:
            flag = True

    if (answer_person == 'y') and (flag is True):
        is_right = True
        for i in range(3):
            if number in person.players_card.my_card[i]:
                index_of_number = person.players_card.my_card[i].index(number)
                person.players_card.my_card[i][index_of_number] = '--'
    elif (answer_person == 'n') and (flag is False):
        is_right = True
    if (answer_person == 'y') and (flag is False) or (answer_person == 'n') and (flag is True):
        print(f'\nНеверный ответ.')

    if answer_person != 'n' and answer_person != 'y':
        print(f'\nНеверный формат ввода. Ознакомьтесь с правилами игры.')

    return is_right


def play(person, computer):
    all_numbers = [x for x in range(1, 91)]
    shuffle(all_numbers)
    count_for_numbs = 0

    print(f'Добро пожаловать в игру!\nКарта компьютера:\n{computer.players_card} '
          f'Карта игрока:\n{person.players_card}')
    count_person = 15
    count_computer = 15
    break_flag = False

    while count_computer > 0 and count_person > 0:
        number, count_for_numbs = choose_number(all_numbers, count_for_numbs)
        print(f'Цифра номер {number}')

        answer_person = person.choice_of_move()
        print(f'Ответ игрока: {answer_person}')
        answer_computer = computer.choice_of_move(number)
        print(f'Ответ компьютера: {answer_computer}')

        if check_answer(person, answer_person, number) is False:
            break_flag = True
            break

        print(f'Карта компьютера:\n{computer.players_card} '
              f'Карта игрока:\n{person.players_card}')
        if answer_person == 'y':
            count_person -= 1
        if answer_computer == 'y':
            count_computer -= 1

    if break_flag is True:
        print('Вы проиграли!')
    elif count_person == 0 and count_computer == 0:
        print('Ничья')
    elif count_person == 0:
        print('Вы выиграли')
    else:
        print('Выиграл компьютер!')

