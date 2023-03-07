a = [2, 3, 4, 7]
b = a
b[2] = 8  # if you make a list equal to another the python creates a connection between them
print('EXAMPLE 1')
print(f'List A: {a}')
print(f'List B: {b}')

# to not create that connection you need to really copy all of the elements from the another list, like that way:
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print('EXAMPLE 2')
print(f'List A: {a}')
print(f'List B: {b}')
