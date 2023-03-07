from time import sleep

firstNum = int(input('Enter a integer number: '))
secondNum = int(input('Enter another integer: '))
continueLoop = True

while continueLoop:
    option = input('''Choose an option:
[ 1 ] sum
[ 2 ] multiply
[ 3 ] greater
[ 4 ] new numbers
[ 5 ] exit the program
Option: ''')
    if option == '1':
        print(f'\n{firstNum} + {secondNum} = {firstNum + secondNum}')
    if option == '2':
        print(f'\n{firstNum} X {secondNum} = {firstNum * secondNum}')
    if option == '3':
        if firstNum > secondNum:
            print(f'\n{firstNum} is the greater number!')
        if secondNum > firstNum:
            print(f'\n{secondNum} is the greater number!')
        if firstNum == secondNum:
            print('\nThe numbers are equal')
    if option == '4':
        firstNum = int(input('\nEnter a integer number: '))
        secondNum = int(input('Enter another integer: '))
    if option == '5':
        continueLoop = False
    sleep(1)
print('Exiting...')
sleep(2)
print('Thanks you for using the program!')
