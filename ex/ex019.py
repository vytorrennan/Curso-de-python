from random import choice
studant1 = input('Enter the name of the first student: ')
studant2 = input('Enter the name of the second student: ')
studant3 = input('Enter the name of the third student: ')
studant4 = input('Enter the name of the fourth student: ')
choicing = choice([studant1, studant2, studant3, studant4])
print('The chosen one is {}'.format(choicing))
