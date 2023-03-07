number = int(input('Enter a integer: '))

penultimate = 0
last = 1
repetitions = 1
print(last, end=', ')
while repetitions < number:
    _sum = penultimate + last
    penultimate = last
    last = _sum
    print(last, end=', ')
    repetitions += 1
print('DONE')
