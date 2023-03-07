from math import trunc
number = float(input('Enter a floating number: '))
print('The integer part of {} is {}'.format(number, trunc(number)))

# or *print('The integer part of {} is {}'.format(number, int(number))* with this method you will not need
# the math library