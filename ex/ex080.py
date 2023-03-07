NumbersList = []
for count in range(0, 5):
    number = int(input('Enter a number: '))
    position = 0
    while True:
        if position > (len(NumbersList) - 1):
            NumbersList.insert(len(NumbersList), number)
            print('Added at the end of the list!')
            break
        if NumbersList[position] > number:
            NumbersList.insert(position, number)
            print(f'Added at the position {position}')
            break
        position += 1
print('-=' * 40)
print(f'The values in order are {NumbersList}')
