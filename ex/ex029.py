velocity = float(input('How fast is your car in km/h? '))
if velocity > 80.0:
    print('You were fined! The fine will cost R${:.2f}'.format((velocity - 80) * 7))
print('Have a nice day and drive safely!')
