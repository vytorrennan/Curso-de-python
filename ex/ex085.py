allNumbers = [[], []]

for c in range(1, 8):
    num = int(input(f'Enter the {c}º number: '))
    if num % 2 == 0:
        allNumbers[1].append(num)
    else:
        allNumbers[0].append(num)
allNumbers[0].sort()
allNumbers[1].sort()
print('=+' * 40)
print(f'The odd numbers entered were: {allNumbers[0]}')
print(f'The even numbers entered were: {allNumbers[1]}')
