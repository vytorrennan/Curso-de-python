option = 0
while option != 5:
    if option == 0:
        number1 = float(input('Enter the first value: '))
        number2 = float(input('Enter the second value: '))
    option = int(input('''[1] SUM
[2] MULTIPLY
[3] GREATER
[4] NEW NUMBERS
[5] STOP THE PROGRAM
What do you wanna do with these numbers? '''))
    if option == 1:
        print(f'\n{number1} + {number2} = {number1 + number2}\n')
    if option == 2:
        print(f'\n{number1} * {number2} = {number1 * number2}\n')
    if option == 3:
        if number1 >= number2:
            print(f'\nThe greater number is {number1}\n')
        else:
            print(f'\nThe grater is {number2}\n')
    if option == 4:
        option = 0
