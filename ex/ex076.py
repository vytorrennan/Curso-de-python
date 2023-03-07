tableThings = ('Pencil', 1.75, 'Eraser', 2.00, 'Notebook', 15.00, 'Case', 25.00, 'Protractor', 4.20, 'Compass', 9.99,
               'Backpack', 120.32, 'Pens', 22.30, 'Book', 34.90)

print('-' * 41)
print(f'{"List of prices!":^41}')
print('-' * 41)

for c in range(0, len(tableThings)):
    if type(tableThings[c]) is str:
        print(f'{tableThings[c]:.<32}R$', end='')
    else:
        print(f'{tableThings[c]:>7.2f}', end='\n')
print('-' * 41)
