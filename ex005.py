import random


def player():
    user = input("Chose one 'r' = rock,'p' = paper e 's' = scissors:")
    computer = random.choice(['r', 'p', 't'])
    if user == computer:
        return 'Tie'
    if is_win(user, computer):
        return 'You win'

    return 'You lost'


def is_win(player, opponent):
    if ((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')
            or (player == 'p' and opponent == 'r')):
        return True
print(player())
