from time import sleep


def greater(*values):
    print('-=' * 30)
    print('Analyzing the numbers...')
    greater_num = 0
    if len(values) > 0:
        greater_num = values[0]
    for value in values:
        sleep(0.4)
        print(value, end=', ')
        if value >= greater_num:
            greater_num = value
    print(f'Were entered {len(values)} values at total.')
    print('The greater one were', greater_num)


greater(2, 9, 4, 5, 7, 1)
greater(4, 7, 0)
greater(1, 2)
greater(6)
greater()
