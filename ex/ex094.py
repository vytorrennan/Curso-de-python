person = dict()
people = list()
average = 0
allWomen = list()

continue_ = 'Y'
while continue_ == 'Y':
    person['name'] = str(input('Name: ')).strip()
    person['sex'] = str(input('Sex: [M/F] ')).strip().upper()
    while person['sex'] != 'M' and person['sex'] != 'F':
        print('Error! Please, enter just M or F.')
        person['sex'] = input('Sex: [M/F] ').strip().upper()[0]
    person['age'] = int(input('Age: ').strip())
    average += person['age']
    if person['sex'][0] == 'F':
        allWomen.append(person['name'])
    people.append(person.copy())
    continue_ = input('Do you want to continue? [Y/N] ').strip().upper()
    while continue_ != 'Y' and continue_ != 'N':
        print('Error! Please, enter just Y or N.')
        continue_ = input('Do you want to continue? [Y/N] ').strip().upper()
print('-=' * 60)
print(f'A) The group have {len(people)} peoples')
average = average / len(people)
print(f'B) The average of age is {average:5.2f}')
print(f'C) The registered women were ', end='')
for women in allWomen:
    print(women, end='...')
print('\nD) List of people who are above average:')
for p in people:
    if p['age'] >= average:
        print(f'     Name: {p["name"]}; Sex: {p["sex"]}; Age: {p["age"]}')
print('<< FINISHED >>')
