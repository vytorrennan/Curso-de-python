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
