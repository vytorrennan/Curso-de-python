times = 0
total = 0
listNumbers = []
userDecision = 'Y'
while userDecision != 'N':
    number = int(input('Enter a integer number: '))
    total += number
    times += 1
    listNumbers.append(number)
    userDecision = input('Do you want to continue (Y / N)? ').upper().strip()[0]
print(f'\nYou enter {times} numbers and the average of these numbers is {total / times:.1f}!')
listNumbers.sort()
print(f'The smallest number is {listNumbers[0]} and the greater is {listNumbers[len(listNumbers) - 1]}!')
