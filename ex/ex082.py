numbers = []
continue_ = 'Y'
odd = []
even = []

while continue_ == 'Y':
    numbers.append(int(input('Enter a number: ')))
    continue_ = input('Want to continue? [Y/N] ').upper()
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print('--' * 40)
print(f'You entered the numbers {numbers}')
print(f'The even numbers are {even}')
print(f'And the odd numbers are {odd}')
