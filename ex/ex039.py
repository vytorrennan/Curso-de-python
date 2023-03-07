from datetime import date
gender = input('Enter M if you are a man and a F if you are a woman: ')
day = int(input('What day were you born? Use numbers please. '))
month = int(input('What month were you born? Use numbers please. '))
year = int(input('What year were you born? '))
age = 0
# to get the age (this is for if the birthday has passed or if it's today)
if month < date.today().month:
    age = date.today().year - year
if month == date.today().month and day <= date.today().day:
    age = date.today().year - year
# to get the age (this is for if the birthday has not yet passed)
if month > date.today().month:
    age = date.today().year - year - 1
if month == date.today().month and day > date.today().day:
    age = date.today().year - year - 1
# checking if it male or female
if gender == 'F':
    print('You don\'t need to enlist, because you are a woman')
    exit()
print('You are {} years old'.format(age))
# comparing the age of the military enlistment and the age of the person
if age == 18:
    print('It\'s time for enlistment')
if age < 18:
    print('{} years until enlistment!'.format(18 - age))
if age > 18:
    print('{} years have passed since the date you were supposed to enlist!'.format(age - 18))
