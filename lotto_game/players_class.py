"""
Класс игроков.

Родительский класс Player проверяет тип карточки при создании.
На вход карточка игрока (тип CardForLoto)

Класс Person - наследующий от Player.
Имеет функцию выбора хода - запрашивает ответ у пользователя.
На вход карточка игрока (от Player). Вывод - ответ пользователя (строка).

Класс Computer - наследующий от Player.
Имеет функцию выбора хода - проверяет наличие числа, дает соответствующий ответ, сама удаляет число
в карточке.
На вход карточка игрока (от Player), число, которое проверить на наличие. Вывод строка с ответом действия.
"""
import cards_class


class Player:
    def __init__(self, players_card):
        if isinstance(players_card, cards_class.CardForLoto):
            self.players_card = players_card
        else:
            raise ValueError('Неправильный тип карточки')


class Person(Player):
    @staticmethod
    def choice_of_move():
        choice = input('Хотите зачеркнуть цифру в своей карточке? "y" - да, "n" - нет\n')
        return choice


class Computer(Player):
    def choice_of_move(self, number):
        flag = False
        for i in range(3):
            if number in self.players_card.my_card[i]:
                flag = True
                index_of_number = self.players_card.my_card[i].index(number)
                self.players_card.my_card[i][index_of_number] = '--'
        if flag is True:
            return 'y'
        else:
            return 'n'
