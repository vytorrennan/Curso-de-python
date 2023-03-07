from datetime import date
year = int(input('Enter any year, or 0 if you want it to be this year: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} is a leap year!'.format(year))
else:
    print('{} is not leap year!'.format(year))
