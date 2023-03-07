from ex.modulos_pacotes.ex109 import coin


def resume(price, percent_i, percent_r):
    print('-' * 37)
    print(f'{"VALUE RESUME":^37}')
    print('-' * 37)
    print(f'Analyzed price:            {coin.coin(price)}')
    print(f'Double of the price:       {coin.double(price)}')
    print(f'Half of the price:         {coin.half(price)}')
    print(f'{percent_i}% of increasing:         {coin.increase(price, percent_i)}')
    print(f'{percent_r}% of reducing:           {coin.reduce(price, percent_r)}')
    print('-' * 37)
