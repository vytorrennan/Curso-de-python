number = int(input('Enter a number: '))
print(
    'The multiplication table of {} is: \n'
    '========================\n'
    'multiplied by 01 is: {:2}\n'
    'multiplied by 02 is: {:2}\n'
    'multiplied by 03 is: {:2}\n'
    'multiplied by 04 is: {:2}\n'
    'multiplied by 05 is: {:2}\n'
    'multiplied by 06 is: {:2}\n'
    'multiplied by 07 is: {:2}\n'
    'multiplied by 08 is: {:2}\n'
    'multiplied by 09 is: {:2}\n'
    'multiplied by 10 is: {:2}\n'
    '========================'
    .format(number, number * 1, number * 2, number * 3, number * 4, number * 5, number * 6, number * 7, number * 8,
            number * 9, number * 10)
)

# print('{} multiplied by 1 is {}'.format(number, number * 1))
# print('{} multiplied by 2 is {}'.format(number, number * 2))
# print('{} multiplied by 3 is {}'.format(number, number * 3))
# print('{} multiplied by 4 is {}'.format(number, number * 4))
# print('{} multiplied by 5 is {}'.format(number, number * 5))
# print('{} multiplied by 6 is {}'.format(number, number * 6))
# print('{} multiplied by 7 is {}'.format(number, number * 7))
# print('{} multiplied by 8 is {}'.format(number, number * 8))
# print('{} multiplied by 9 is {}'.format(number, number * 9))
# print('{} multiplied by 10 is {}'.format(number, number * 10))
