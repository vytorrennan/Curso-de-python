def half(p, is_money=True):
    result = p / 2
    return result if not is_money else coin(result)


def double(p, is_money=True):
    result = p * 2
    return result if not is_money else coin(result)


def increase(p, percent, is_money=True):
    result = ((p * percent) / 100) + p
    return result if not is_money else coin(result)


def reduce(p, percent, is_money=True):
    result = p - ((p * percent) / 100)
    return result if not is_money else coin(result)


def coin(p=0, money='R$'):
    return f'{money}{p:,.2f}'.replace('.', ',')


def resume(price, percent_i, percent_r):
    print('-' * 37)
    print(f'{"RESUME OF THE VALUE":^37}')
    print('-' * 37)
    print(f'Analyzed price:            {coin(price)}')
    print(f'Double of the price:       {double(price)}')
    print(f'Half of the price:         {half(price)}')
    print(f'{percent_i}% of increasing:         {increase(price, percent_i)}')
    print(f'{percent_r}% of reducing:           {reduce(price, percent_r)}')
    print('-' * 37)
