from time import sleep

sum_ = 0
count = 0
for c in range(1, 7):
    number = int(input('Enter a integer number: '))
    sleep(0.2)
    if number % 2 == 0:
        count += 1
        sum_ += number
print(f'Among these numbers, {count} are even')
print('of these numbers adding only even numbers, the result would be', sum_)
