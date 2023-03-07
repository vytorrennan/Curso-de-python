number = str(input('Enter a number from 0 to 9999: ') + '000')
n = number.split(',')
print('''units: {} 
tens: {}
hundreds: {}
thousands: {}'''.format(number[number.rfind('0') - 3], number[number.rfind('0') - 4], number[number.rfind('0') - 5], number[number.rfind('0') - 6]))


#.zfill(4) = ele completa com zeros ate o numero de casas q vc precisa
