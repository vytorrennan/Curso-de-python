numbers = []
continue_ = 'Y'

while continue_ == 'Y':
    numbers.append(int(input('Enter a number: ')))
    continue_ = input('Want to continue? [Y/N] ').upper().strip()
print('--' * 40)
print(f'You enter {len(numbers)} numbers!')
numbers.sort(reverse=True)
print(f'In descending order is {numbers}')
if 5 not in numbers:
    print('Don\'t have a 5 in the list!')
else:
    print('Have a 5 in the list!')
