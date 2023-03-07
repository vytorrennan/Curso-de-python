def half(p=0):
    return p / 2


def double(p=0):
    return p * 2


def increase(p=0, percent=0):
    return ((p * percent) / 100) + p


def reduce(p=0, percent=0):
    return p - ((p * percent) / 100)


def coin(p=0, money='R$'):
    return f'{money}{p:,.2f}'.replace('.', ',')
