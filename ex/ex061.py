firstTerm = int(input('Enter the first term PA: '))
reason = int(input('Enter the PA reason: '))

PA = firstTerm
times = 1
while times <= 10:
    print(f'{PA} -> ', end='')
    PA = PA + reason
    times += 1
print('Finish')
