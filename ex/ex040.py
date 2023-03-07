grade1 = float(input('Enter the first grade: '))
grade2 = float(input('Enter the second grade: '))
average = (grade1 + grade2) / 2
print('Your average was {:.1f}'.format(average))
if average < 5.0:
    print('You was reproved!')
if 5.0 <= average < 6.9:
    print('You are in recuperation!')
if average >= 7.0:
    print('You are approved!')
