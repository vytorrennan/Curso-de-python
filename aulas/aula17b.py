# values = list() it's the same as value = []
values = []
values.append(5)
values.append(9)
values.append(4)

print(values)
for value in values:
    print(f'{value}...', end='')

for position, value in enumerate(values):  # now you can take the position and the value at the same time
    print(f'In the position {position} i find the value {value}!')
print('i achive the end of the list.')
