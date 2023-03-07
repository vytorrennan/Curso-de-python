# taking the number of sides of the triangle
n1 = float(input('Enter a number to the triangle: '))
n2 = float(input('Enter another number to the triangle: '))
n3 = float(input('Enter one more number to the triangle: '))
# to organize them in ascending order
organization = [n1, n2, n3]
organization.sort()
# checking what type of triangle can be created
equtriangle = n1 == n2 == n3
isotriangle = n1 == n2 or n1 == n3 or n2 == n3
scatriangle = n1 != n2 != n3 != n1
if organization[2] < organization[0] + organization[1]:
    if equtriangle:
        print('You can make a equilateral triangle with these numbers!')
    elif isotriangle:
        print('You can make a isosceles triangle with these numbers!')
    elif scatriangle:
        print('You can make a scalene triangle with these numbers!')
else:
    print('You can\'t make a triangle with these numbers!')
