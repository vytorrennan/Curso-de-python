times = -1
total = 0
number = 0
while number != 999:
    total += number
    times += 1
    number = int(input('Enter a integer number(Enter 999 when you want to finish): '))
print('~' * 47)
print(f'You enter {times} numbers!')
print(f'The result of adding these numbers is {total}')
print('~' * 47)
