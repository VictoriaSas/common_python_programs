"""
Вызовы для начала игры.
"""
import players_class
import cards_class
import play_game


person_card = cards_class.CardForLoto()
computer_card = cards_class.CardForLoto()
my_person = players_class.Person(person_card)
comp = players_class.Computer(computer_card)
play_game.play(my_person, comp)
