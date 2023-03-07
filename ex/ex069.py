# variables
person = 1
plus18 = men = womenLess20 = 0

while True:
    print('=+' * 12)
    print('      REGISTRATION')
    print('=+' * 12)
    # collecting the information correctly
    age = int(input(f'Enter the age of the {person}ª person: '))
    sex = input(f'Enter the sex of the {person}ª person: [M / F] ').strip().upper()[0]
    while sex not in 'MF':
        print('Please choose Male or Female!')
        sex = input(f'Enter the sex of the {person}ª person: [M / F] ').strip().upper()[0]

    # checking the information according to the parameters
    if age >= 18:
        plus18 += 1
    if sex == 'M':
        men += 1
    if age < 20 and sex == 'F':
        womenLess20 += 1

    # asking if the user wants to add someone else
    wantContinue = input('Do you want to add another person? [Y / N] ').strip().upper()[0]
    while wantContinue not in 'YN':
        print('Please enter something valid!')
        wantContinue = input('Do you want to add another person? [Y / N] ').strip().upper()[0]
    if wantContinue == 'N':
        break
    person += 1

# showing the information according to the parameters
print('==' * 19)
print(f'{plus18} of these people are over 18')
print(f'{men} of these people are men')
print(f'{womenLess20} of then are women under 20')
print('==' * 19)
