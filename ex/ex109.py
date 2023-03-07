from modulos_pacotes.ex109 import coin

price = float(input('Enter the price: R$'))
print(f'Half of {coin.coin(price)} is {coin.half(price, True)}')
print(f'The double of {coin.coin(price)} is {coin.double(price, True)}')
print(f'increasing 10%, we have {coin.increase(price, 10, True)}')
print(f'reducing 13%, we have {coin.reduce(price, 13, True)}')
