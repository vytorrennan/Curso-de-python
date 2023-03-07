import numbersystem
number = int(input('Enter a Integer: '))
decision = int(input('if you want to convert for:\nbinary enter 1 \noctal enter 2 \nHexadecimal enter 3: '))
if decision != 1 and decision != 2 and decision != 3:
    print('Please choose a valid conversion number')
if decision == 1:
    print('{} converted to binary is {}'.format(number, numbersystem.decimalToBinary(number)))
if decision == 2:
    print('{} converted to octal is {}'.format(number, numbersystem.decimalToOctal(number)))
if decision == 3:
    print('{} converted to hexadecimal is {}'.format(number, numbersystem.decimalToHexa(number)))

# you can use these native functions of the python too
# bin()
# hex()
# oct()
