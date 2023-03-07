numbers = []
for count in range(0, 5):
    numbers.append(int(input(f'Enter a number to the position {count}: ')))
originalNumbers = numbers[:]
numbers.sort()

print('-='*40)
print(f'You enter the values {originalNumbers}')
print(f'The smaller one is {numbers[0]} in the position ', end='')
for position, num in enumerate(originalNumbers):
    if num == numbers[0]:
        print(f'{position}... ', end='')
print(f'\nand the greatest one is {numbers[4]} in the position ', end='')
for position, num in enumerate(originalNumbers):
    if num == numbers[4]:
        print(f'{position}... ', end='')
