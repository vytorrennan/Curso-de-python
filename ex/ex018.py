from math import cos, sin, tan, radians
angle = float(input('Enter the angle: '))
radian = radians(angle)
sine = sin(radian)
cosine = cos(radian)
tangent = tan(radian)
print('The sine of that angle is {:.2f} the cosine is {:.2f} and the tangent is {:.2f}'.format(sine, cosine, tangent))
