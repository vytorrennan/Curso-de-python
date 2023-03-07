from datetime import datetime

year = datetime.today().year
person = {'name': input('Name: '),
          'age': year - int(input('Year of birth: ')),
          'work card': int(input('Work card (0 if you don\'t have it): '))}
if person['work card'] != 0:
    person['year of hiring'] = int(input('Year of hiring: '))
    person['salary'] = float(input('Salary: R$ '))
    person['retirement'] = person['age'] + ((person['year of hiring'] + 35) - year)
print('-=' * 21)
for k, v in person.items():
    print(f'  - {k} have value {v}')
