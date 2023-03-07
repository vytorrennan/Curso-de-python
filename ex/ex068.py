from random import randint

winner = ''
userWins = 0

print('=+' * 12)
print('LET\'S PLAY ODD AND EVEN')
print('=+' * 12)
while True:
    userNum = int(input('Enter the number: '))
    userOddOrEven = input('You want odd or even? [O or E] ').strip().upper()[0]
    while userOddOrEven not in 'OE':
        print('Please choose odd or even!')
        userOddOrEven = input('You want odd or even? [O or E] ').strip().upper()[0]
    compNum = randint(0, 10)
    print(f'\nUser: {userNum} & Computer: {compNum} --- The total is {userNum + compNum}')
    if (userNum + compNum) % 2 == 0:
        winner = 'E'
        print('EVEN WON!!!\n')
    else:
        print('ODD WON!!!\n')
    if userOddOrEven == winner:
        userWins += 1
        print('==' * 12)
        print('YOU WON! Let\'s play more')
        print('==' * 12)
    if userOddOrEven != winner:
        print('==' * 12)
        print('You lose, try again next time.')
        break
print(f'You won {userWins} times!')
print('==' * 12)
