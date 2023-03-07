n = 1
pair = odd = 0  # this is basically the same as pair = 0 and odd = 0
while n != 0:
    n = int(input('Enter a value: '))
    if n != 0:
        if n % 2 == 0:
            pair += 1
        else:
            odd += 1
print(f'You enter {pair} pair numbers, and {odd} odd numbers!')
