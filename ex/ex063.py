howMany = int(input('How many elements of the Fibonacci sequence you want see? '))

n2 = 0
number = 1
times = 2

print(f'{n2} -> {number} -> ', end='')
continueLoop = True
while continueLoop:
    number = n2 + number
    n2 = number - n2
    print(f'{number} -> ', end='')
    times += 1
    if times == howMany:
        continueLoop = False
print('finish')
