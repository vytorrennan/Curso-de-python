def read_money(text):
    while True:
        a = input(text).strip()
        if a.replace('.', '').replace(',', '').isnumeric():
            return float(a.replace(',', '.'))
        else:
            print('ERROR')
