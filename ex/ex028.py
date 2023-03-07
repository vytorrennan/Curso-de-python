from random import randrange
number = randrange(6)
userAnswer = int(input('what integer between 0 and 5 is the computer thinking about? '))
if userAnswer == number:
    print('Congratulations!, you won!')
else:
    print('You lose, try again in the next time!')
