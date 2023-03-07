from time import sleep


def counter(begin, end, step):
    print('-=' * 20)
    print(f'counter from {begin} to {end}, {abs(step)} by {abs(step)}')
    sleep(1.5)
    if begin > end:
        end -= 2
        if step > 0:
            step = -step
    if step == 0 and begin < end:
        step = 1
    elif step == 0 and begin > end:
        step = -1
    for numbers in range(begin, end + 1, step):
        sleep(0.2)
        print(numbers, end=', ')
    print('END!')


counter(1, 10, 1)
counter(10, 0, -2)
print('-=' * 20)
print('Now it\'s your turn')
counter(int(input('Begin: ')), int(input('End: ')), int(input('Step: ')))
