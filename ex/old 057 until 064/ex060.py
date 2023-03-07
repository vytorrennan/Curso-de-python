number = int(input('Enter the number: '))
number2 = number
number2 = number2 * (number - 1)
print(f'{number} x {number - 1}')
while number != 0:
    number -= 1
    if number - 1 == 0:
        break
    print(f'{number} x {number - 1}')
    number2 = number2 * (number - 1)
print(f'The factorial of this number is {number2}')
