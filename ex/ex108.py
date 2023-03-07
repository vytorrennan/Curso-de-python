from modulos_pacotes.ex108 import coin

price = float(input('Enter the price: R$'))
print(f'Half of {coin.coin(price)} is {coin.coin(coin.half(price))}')
print(f'The double of {coin.coin(price)} is {coin.coin(coin.double(price))}')
print(f'increasing 10%, we have {coin.coin(coin.increase(price, 10))}')
print(f'reducing 13%, we have {coin.coin(coin.reduce(price, 13))}')
