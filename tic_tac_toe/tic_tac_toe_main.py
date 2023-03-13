import tic_tac_toe_func


field_position = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
winning_combinations = ('159', '123', '147', '258', '357', '369', '456', '789')
if tic_tac_toe_func.play(field_position, winning_combinations) is True:
    print('finish')
