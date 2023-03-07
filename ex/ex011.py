from math import ceil, sqrt

width = float(input('the width of the wall: '))
height = float(input('the height of the wall: '))
area = width * height
litersOfInk = ceil(area / 2)
print('You will need {} liters of ink'.format(litersOfInk))

print('you can use the from import to import more them just 1 module using the comma after the first module {}'.format(sqrt(4)))
#if you use just import math, the comand will not be cell() will be math.ceil()
