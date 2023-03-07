housevalue = float(input('How much does the house cost? R$'))
salary = float(input('What\'s the the buyer\'s salary? R$'))
yearstopay = float(input('In how many years will wanna pay? ')) * 12
installments = (housevalue / yearstopay)
thirtypercent = salary * 30 / 100
if installments > thirtypercent:
    print('You can\'t buy these house, because the installments are more than 30% of your salary!')
else:
    print('Okay, you can buy this house!')
print('Have a nice day!')
