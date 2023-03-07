guys = []
person = []
count = 0
continue_ = 'Y'

while continue_[0] == 'Y':
    count += 1
    person.append(input(f'Enter the name of the {count}ª person: '))
    person.append(input(f'Enter the weight of the {count}ª person: '))
    guys.append(person[:])
    person.clear()
    continue_ = input('Wanna continue? [Y/N] ').strip().upper()

print(f'You entered {count} persons')
mostWeight = guys[0][1]
lessWeight = guys[0][1]
for c in range(0, len(guys)):
    if guys[c][1] >= mostWeight:
        mostWeight = guys[c][1]
    if guys[c][1] <= lessWeight:
        lessWeight = guys[c][1]
print(f'The greater weight was {mostWeight} from', end=' ')
for c in range(0, len(guys)):
    for pos, num in enumerate(guys[c]):
        if mostWeight == num:
            print(guys[c][0], end='...')
print(f'\nThe smallest weight was {mostWeight} from', end=' ')
for c in range(0, len(guys)):
    for pos, num in enumerate(guys[c]):
        if lessWeight == num:
            print(guys[c][0], end='...')
