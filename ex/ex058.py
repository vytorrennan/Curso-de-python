from random import randint

number = randint(0, 10)
timesTried = 0
wrongAnswer = True
while wrongAnswer:
    timesTried += 1
    userAnswer = int(input('Try to guess the number the computer is thinking between 0 and 10: '))
    if userAnswer == number:
        print('CONGRATULATIONS!!! You hit the number!')
        print(f'You tried {timesTried} times')
        wrongAnswer = False
    else:
        if userAnswer < number:
            print('it\'s greater')
        if userAnswer > number:
            print('it\'s smaller')
        print('WRONG NUMBER! Try again')

'''
existe tbm o 
while not
q é enquanto não, muito util tbm
'''