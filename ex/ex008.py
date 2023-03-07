meters = float(input('Enter the meters: '))
kilo = meters / 1000
acre = meters / 10000
deca = meters / 10
deci = meters * 10
cen = meters * 100
mili = meters * 1000
print('these meters in centimeters is {:.0f} and in milimeters it is {:.0f}'.format(cen, mili))
print('in kilometers is {} in acres is {} in decameters is {} in decimeters is {}'.format(kilo, acre, deca, deci))
