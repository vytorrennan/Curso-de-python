n1 = float(input('Enter a number: '))
n2 = float(input('Enter another number: '))
n3 = float(input('Enter one more number: '))
organization = [n1, n2, n3]
organization.sort()
if organization[2] < organization[0] + organization[1]: 
    print('You can make a triangle with these numbers!')
else:
    print('You can\'t make a triangle with these numbers!')
