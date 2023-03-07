number = int(input('Enter the number you want to see the factorial: '))
originalNumber = number
second = number - 1
continueLoop = True

print('+=' * 14)
print(f'{number} * {second} = ', end='')
number = number * second
print(number)
while continueLoop:
    second -= 1
    if second == 1:
        continueLoop = False
    print(f'{number} * {second} = ', end='')
    number = number * second
    print(number)
print(f'\nThe factorial of {originalNumber} is {number}')
print('+=' * 14)
