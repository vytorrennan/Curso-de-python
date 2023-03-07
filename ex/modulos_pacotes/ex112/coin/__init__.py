def half(p, is_money=True):
    if is_money:
        return f'R${p / 2:,.2f}'.replace('.', ',')
    return p / 2


def double(p, is_money=True):
    if is_money:
        return f'R${p * 2:,.2f}'.replace('.', ',')
    return p * 2


def increase(p, percent, is_money=True):
    if is_money:
        return f'R${((p * percent) / 100) + p:,.2f}'.replace('.', ',')
    return ((p * percent) / 100) + p


def reduce(p, percent, is_money=True):
    if is_money:
        return f'R${p - ((p * percent) / 100):,.2f}'.replace('.', ',')
    return p - ((p * percent) / 100)


def coin(p):
    return f'R${p:,.2f}'.replace('.', ',')


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
