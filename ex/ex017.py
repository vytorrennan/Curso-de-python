from math import hypot
cO = float(input('The opposite side: '))
cA = float(input('The adjacent side: '))
hypotenuse = hypot(cO, cA)
print('The hypotenuse is {:.2f}'.format(hypotenuse))
