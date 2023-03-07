print(f'{"ALIEXPRESS":=^40}')
print(f'{"ALIEXPRESS":=^40}')
print(f'{"ALIEXPRESS":=^40}')
price = float(input('Enter the normal price: R$'))
methods = int(input('''Enter de payment method:
{}cash / check: 10% discount{}--------------(Enter 1 to select this method)
{}cash on card: 5% discount{}---------------(Enter 2 to select this method)
{}up to 2x on the card: normal price{}------(Enter 3 to select this method)
{}3x or more on the card: 20% interest{}----(Enter 4 to select this method)
{}Method{}: '''.format('\033[4m', '\033[m', '\033[4m', '\033[m', '\033[4m', '\033[m', '\033[4m', '\033[m', '\033[33m',
                       '\033[m')))

percent = 0  # will be the percent of discount or interest

# if the user don't choose 1, 2, 3 or 4
if methods != 1 and methods != 2 and methods != 3 and methods != 4:
    print('Please choose a valid payment method')
    exit()

if methods == 1:
    percent = -(price * 10 / 100)  # method 1, the normal price with 10% discount
if methods == 2:
    percent = -(price * 5 / 100)  # method 2, the normal price with 5% discount
if methods == 3:
    percent = 0  # method 3, the normal price with nothing
    split = price / 2
    print(f'Your purchase will be split in 2x of \033[32mR${split:.2f}\033[m without interest')
if methods == 4:
    percent = price * 20 / 100  # method 4, the normal price with 20% interest
    split = int(input('How many time will you divide? '))
    print(f'You purchase will be split in {split}x of \033[32mR${(price + percent) / split:.2f}\033[m')

print('The final price will be \033[32mR${:.2f}'.format(price + percent))
