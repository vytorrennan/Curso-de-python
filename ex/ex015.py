days = int(input('For many days did you rented the car? '))
kilo = float(input('Did you drive the car for many kilometers? '))
finalResult = (days * 60) + (kilo * 0.15)
print('You will need to pay R${:.2f}'.format(finalResult))
