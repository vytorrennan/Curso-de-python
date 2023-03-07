number = int(input('Enter a number: '))
print('The multiplication table of {} is:')
print('=' * 24)
for c in range(1, 11):
    print(f'Multiplied by: {c:2} is \033[32m{c * number:2}\033[m')
print('=' * 24)
