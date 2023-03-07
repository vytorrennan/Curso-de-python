from random import randint
from time import sleep

data = {'Player 1': randint(1, 6),
        'Player 2': randint(1, 6),
        'Player 3': randint(1, 6),
        'Player 4': randint(1, 6)}
print('Values:')
for key, values in data.items():
    print(f'    {key}: {values}')
    sleep(1)
print(f'The ranking is:')
greaterValue = -1
GreaterValueKey = ''
count = 0
while True:
    first = True
    for k, v in data.items():
        if v >= greaterValue or first:
            first = False
            greaterValue = v
            GreaterValueKey = k
    count += 1
    print(f' {count}º {GreaterValueKey}: {greaterValue}')
    sleep(1)
    del data[GreaterValueKey]
    if len(data) == 0:
        break

#  He does at this way in the video:
#
#  from operator import itemgetter
#  ranking = sorted(data.items(), key=itemgetter(1), reverse=True)d
