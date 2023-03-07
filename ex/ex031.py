distance = float(input('what is the trip distance in km/h? '))
if distance <= 200:
    print('The trip will cost R${:.2f}'.format(distance * 0.50))
else:
    print('The trip will cost R${:.2f}'.format(distance * 0.45))
