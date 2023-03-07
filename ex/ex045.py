from random import choice
from time import sleep

userDecision = input('\033[36mChoose rock, paper or scissors: \033[m').strip().title()
computerDecision = choice(['Rock', 'Paper', 'Scissors'])

# "ROCK PAPER SCISSORS!" screen
print('-=' * 20)
print('          \033[35mROCK PAPER SCISSORS!\033[m')
print('-=' * 20)
sleep(1)

# if the user don't choose rock, paper or scissors
if userDecision != 'Rock' and userDecision != 'Paper' and userDecision != 'Scissors':
    print('\033[31mPlease choose a valid option!\033[m')
    exit()

# the visual part of the game
print('{}{}{} X {}{}{}\n'.format('\033[34m', userDecision, '\033[m', '\033[31m', computerDecision, '\033[m'))
sleep(0.7)
if userDecision == 'Rock' and computerDecision == 'Scissors' or userDecision == 'Paper' and computerDecision == 'Rock' or userDecision == 'Scissors' and computerDecision == 'Paper':
    print('{}YOU WIN, CONGRATULATIONS!!!{}'.format('\033[4;32m', '\033[m'))
elif computerDecision == 'Rock' and userDecision == 'Scissors' or computerDecision == 'Paper' and userDecision == 'Rock' or computerDecision == 'Scissors' and userDecision == 'Paper':
    print('{}The computer win, you {}LOSE{}'.format('\033[33m', '\033[4m', '\033[m'))
else:
    print('{}DRAW, Try again!{}'.format('\033[4m', '\033[m'))
print('-=' * 20)
