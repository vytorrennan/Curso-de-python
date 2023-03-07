numbers = []

continue_ = 'Y'
while continue_ == 'Y':
    number = (int(input('Enter a value: ')))
    if number not in numbers:
        numbers.append(number)
        print('Done!')
    else:
        print('This number is already in the list!')
    continue_ = input('do you wanna continue? [Y/N] ').upper().strip()

print('-='*40)
numbers.sort()
print(f'You added numbers {numbers}')
