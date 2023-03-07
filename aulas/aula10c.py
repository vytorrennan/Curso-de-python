# This is a better version of the activity 07:
n1 = float(input('Enter the first grade: '))
n2 = float(input('Enter the second grade: '))
n = (n1 + n2)/2
print('Your average was {:.1f}'.format(n))
if n >= 6.0:
    print('Your average was good! CONGRATULATIONS!')
else:
    print('Your average was bad! STUDY MORE!')

# you can do with this too, it's more simple but more difficult to read
print('CONGRATULATIONS!' if n >= 6.0 else 'STUDY MORE!')