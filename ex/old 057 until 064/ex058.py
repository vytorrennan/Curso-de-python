from random import randint

number = randint(0, 10)
howManyTimes = 0
won = False
while not won:
    howManyTimes += 1
    userAnswer = int(input('what integer between 0 and 10 is the computer thinking about? '))
    if userAnswer == number:
        print('Congratulations!, you won!')
        print(f'You had to try {howManyTimes} times, to win')
        won = True
    else:
        print('no, try again')
