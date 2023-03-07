# variables
totalPrice = plus1000 = 0
cheapest = ['', 0]

print('=+' * 12)
print('      SUPERMARKET!')
print('=+' * 12)

while True:
    # collecting the information correctly
    prodName = input('Enter the name of the product: ').strip()
    prodPrice = float(input('Enter the price of the product: R$'))

    # checking the information according to the parameters
    totalPrice += prodPrice
    if prodPrice > 1000:
        plus1000 += 1
    if prodPrice < cheapest[1] or cheapest[1] == 0:
        cheapest = [prodName, prodPrice]

    # asking if the user wants to add something else
    wantContinue = input('You want to add more products? [Y / N] ').strip().upper()[0]
    while wantContinue not in 'YN':
        wantContinue = input('You want to add more products? [Y / N] ').strip().upper()[0]
    print('')
    if wantContinue == 'N':
        break

# showing the information according to the parameters
print('==' * 19)
print(f'The total price was {totalPrice:.2f}')
print(f'Have {plus1000} products that cost more than R$1000.00')
print(f'The cheapest product was the {cheapest[0]} coasting R${cheapest[1]:.2f}')
print('==' * 19)
