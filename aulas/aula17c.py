values = []
for count in range(0, 5):
    values.append(int(input('Enter a value: ')))

for position, value in enumerate(values):  # now you can take the position and the value at the same time
    print(f'In the position {position} i find the value {value}!')
print('i achive the end of the list.')
