print('Enter a negative number to exit the program!')
while True:
    n = int(input('Do you wanna see the multiplication table of which number? '))
    print('-' * 21)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {n * c}')
    print('-' * 21)
print('\nExited the program')
