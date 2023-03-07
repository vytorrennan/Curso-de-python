from modulos_pacotes.ex107 import coin

price = float(input('Enter the price: R$'))
print(f'Half of {price} is {coin.half(price)}')
print(f'The double of {price} is {coin.double(price)}')
print(f'increasing 10%, we have {coin.increase(price, 10)}')
print(f'reducing 13%, we have {coin.reduce(price, 13)}')
