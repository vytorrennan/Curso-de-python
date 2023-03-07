from datetime import date
year = int(input('What year were you born? '))
age = date.today().year - year
print(f'The athlete is {age} years old')
if age < 9:
    print('You are a MIRIM!')
elif age < 14:
    print('Your are a INFANTIL!')
elif age < 19:
    print('You are a JUNIOR!')
elif age <= 20:
    print('You are a SÊNIOR!')
elif age > 20:
    print('You are a MASTER!')

# the challenge was changed in the correction, with the version of the correction, will be:
# from datetime import date
# year = int(input('What year were you born? '))
# age = date.today().year - year
# print(f'The athlete is {age} years old')
# if age <= 9:
#     print('You are a MIRIM!')
# elif age <= 14:
#     print('Your are a INFANTIL!')
# elif age <= 19:
#     print('You are a JUNIOR!')
# elif age <= 25:
#     print('You are a SÊNIOR!')
# elif age > 25:                       # you can also use a else here
#     print('You are a MASTER!')
