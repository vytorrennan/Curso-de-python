price = float(input('What\'s the price? R$'))
percent = price - (price * 5 / 100)
print('R${} with 5% of discount is R${:.2f}'.format(price, percent))
