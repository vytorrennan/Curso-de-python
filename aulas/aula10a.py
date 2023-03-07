time = int(input('How old is your car? '))
if time <= 3:
    print('new car')
else:
    print('old car')
print('--END--')

# simple version:

time = int(input('How old is your car? '))
print('new car' if time <= 3 else 'old car')
print('--END--')