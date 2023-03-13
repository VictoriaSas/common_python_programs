from random import randrange


def end_game_check(card_now, winning_combinations, field_position):     # Проверка карточки
    # Проверка на выигрыш
    for i in winning_combinations:
        count_o = 0
        count_x = 0
        for el in i:
            if field_position[int(el) - 1] == 'o':
                count_o += 1
            if field_position[int(el) - 1] == 'x':
                count_x += 1
        if count_x == 3:
            print('Выиграли крестики')
            return False
        if count_o == 3:
            print('Выиграли нолики')
            return False

    # Проверка на заполненность карточки (не осталось полей = ничья)
    flag = False
    for i in range(1, 10):
        if str(i) in card_now:
            flag = True
    if flag is False:
        print('Ничья')
    return flag


def game_card(somebodies_value, card_now, whose_move, field_position):     # Заполнение карточки
    move = True
    if (field_position[whose_move - 1] != 'x') and (field_position[whose_move - 1] != 'o') is True:
        field_position[whose_move-1] = somebodies_value
        card_now = card_now.replace(str(whose_move), somebodies_value)
    else:
        print('Это поле уже занято')
        move = False
    return move, card_now


def player_turn(player_value, card_now, field_position):                    # Ход игрока
    print('Ход игрока')
    card_now = player_action(player_value, card_now, field_position)
    print(f'Карта сейчас: \n{card_now}\n')
    return card_now


def player_action(player_value, card_now, field_position):                  # Действие игрока (ввод поля)
    try:
        player_move = int(input('Введите номер области, куда хотите поставить свой знак: '))
    except ValueError:
        print('Неверный формат ввода. Попробуйте еще раз.')
        player_action(player_value, card_now, field_position)
    happened, card_now = game_card(player_value, card_now, player_move, field_position)
    if happened is False:
        player_action(player_value, card_now, field_position)
    return card_now


def computer_turn(computer_value, player_value, card_now, winning_combinations, field_position):    # Ход компьютера
    print('Ход компьютера')
    card_now = computer_action(computer_value, player_value, card_now, winning_combinations, field_position)
    print(f'Карта сейчас: \n{card_now}')
    return card_now


def computer_action(computer_value, player_value, card_now, winning_combinations, field_position):  # Действие компьютера (ввод поля)

    for i in winning_combinations:
        count_comp = 0
        count_player = 0
        for el in i:
            if field_position[int(el) - 1] == computer_value:
                count_comp += 1
            if count_comp == 2:
                for found_numb in i:
                    if field_position[int(found_numb) - 1] != computer_value and field_position[int(found_numb) - 1] != player_value:
                        computer_move = int(found_numb)
                        _, card_now = game_card(computer_value, card_now, computer_move, field_position)
                        return card_now  # end comp act
            if field_position[int(el) - 1] == player_value:
                count_player += 1
            if count_player == 2:
                for found_numb in i:
                    if field_position[int(found_numb) - 1] != computer_value and field_position[int(found_numb) - 1] != player_value:
                        computer_move = int(found_numb)
                        _, card_now = game_card(computer_value, card_now, computer_move, field_position)
                        return card_now  # end comp act

    for i in winning_combinations:
        count_comp = 0
        count_player = 0
        for el in i:
            if field_position[int(el) - 1] == computer_value:
                count_comp += 1
            if field_position[int(el) - 1] == player_value:
                count_player += 1
        if count_comp == 1 and count_player == 0:
            for el in i:
                if field_position[int(el) - 1] != computer_value:
                    computer_move = int(field_position[int(el) - 1])
                    _, card_now = game_card(computer_value, card_now, computer_move, field_position)
                    return card_now  # end comp act

    selection = []
    for el in range(1, 10):
        if (field_position[el-1] != 'x') and (field_position[el-1] != 'o') is True:
            selection.append(el)
    computer_move = selection[randrange(len(selection))]
    _, card_now = game_card(computer_value, card_now, computer_move,field_position)
    return card_now


def play(field_position, winning_combinations):
    print('Добро пожаловать в игру "Крестики-нолики". Сегодня вы играете против компьютера.\nПервый, выстроивший в ряд '
          '3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.\nПервый ход делает игрок, ставящий '
          'крестики. В свой ход выбирайте незаполненную область,\nв которую хотите поставить свой знак.\n')
    print('Ваша карта:')
    card = ' 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n'
    print(card)

    if randrange(0, 2) == 0:
        player = 'x'
        computer = 'o'
        print('Первый ход крестиками у игрока')
    else:
        computer = 'x'
        player = 'o'
        print('Первый ход крестиками у компьютера')

    while True:
        if player == 'x':
            card = player_turn(player, card, field_position)
            if end_game_check(card, winning_combinations, field_position) is not True:
                return True
            card = computer_turn(computer, player, card, winning_combinations, field_position)
            if end_game_check(card, winning_combinations, field_position) is not True:
                return True
        else:
            card = computer_turn(computer, player, card, winning_combinations, field_position)
            if end_game_check(card, winning_combinations, field_position) is not True:
                return True
            card = player_turn(player, card, field_position)
            if end_game_check(card, winning_combinations, field_position) is not True:
                return True
