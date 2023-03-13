"""
Создайте программу для игры с конфетами человек против бота.
На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

Решение (ход компьютера):
Т.к. за один ход нельзя забирать более 28 конфет, то в последний ход у игрока должно быть 1993 конфеты. Точно не сможет
сделать подобный ход игрок, который попал на отметку 1992 (даже если возьмет максимум, то нехватит одной конфеты).
Если игрок попадет на отметку 1991 и ранее на 28, сможет избежать отметки 1992 "подбросив" ее сопернику. Значит каждая
29я комбинация ведет к проигрышу. Самая первая проигрышная отметка - 20.
Выигрышная стратегия: в свой ход выкладывать столько конфет, сколько понадобится до проигрышной отметки (каждая 29ая
с точки отсчета 20.
Следовательно, кто первый ходит, тот выигрывает.
"""

from random import randint
from sys import exit


def check_candies(number_candies, player):
    if number_candies >= 2021:
        print(f'Выиграл {player}!')


def player_turn(numb_of_cands, choices):
    numb_of_cands += choices
    print(f'Ход игрока: {choices}')
    print(f'Стало {numb_of_cands} конфет\n')
    return numb_of_cands


def main_players(numb_of_cands):
    try:
        players_choice = int(input('Введите желаемое количество конфет: '))
    except ValueError:
        print('Неверный формат значение')
        exit()
    # players_choice = randint(1, 28)
    while players_choice < 1 or players_choice > 28:
        print('Неверно задано значение. Попробуйте еще раз')
        players_choice = int(input('Введите желаемое количество конфет: '))
    numb_of_cands = player_turn(numb_of_cands, players_choice)
    return numb_of_cands


def computer_turn(numb_of_cands):   # каждые 29 проеб начиная с 20
    if 0 < numb_of_cands < 20:
        comp_move = 20 - numb_of_cands
        numb_of_cands += comp_move
    else:
        if (numb_of_cands - 20) % 29 != 0:
            exc_case = (numb_of_cands - 20) // 29 + 1
            exc_numb = exc_case * 29 + 20
            comp_move = exc_numb - numb_of_cands
            numb_of_cands += comp_move

        elif (numb_of_cands - 20) % 29 == 0:
            comp_move = randint(1, 28)
            numb_of_cands += comp_move
    print(f'Ход компьютера: {comp_move}')
    print(f'Стало {numb_of_cands} конфет\n')
    return numb_of_cands


def main_computers(numb_of_cands):
    numb_of_cands = computer_turn(numb_of_cands)
    return numb_of_cands


print('Добро пожаловать в игру с конфетами.\n\nПравила:\nНа столе лежит 2021 конфета. Играют игрок и компьютер делая '
      'ход друг после друга. Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет. '
      'Все конфеты оппонента достаются сделавшему последний ход. Выигрывает тот, у кого останутся все конфеты.\n')
numb_of_candies = 2021
candies = 0
whos_first = randint(0, 1)
if whos_first == 0:
    print('Игру начинает игрок\n')
    while candies < numb_of_candies:
        candies = main_players(candies)
        check_candies(candies, 'игрок')
        if candies >= 2021:
            exit()
        candies = main_computers(candies)
        check_candies(candies, 'компьютер')
else:
    print('Игру начинает компьютер\n')
    while candies < numb_of_candies:
        candies = main_computers(candies)
        check_candies(candies, 'компьютер')
        if candies >= 2021:
            exit()
        candies = main_players(candies)
        check_candies(candies, 'игрок')
