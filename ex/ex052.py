number = int(input('Enter a number to check if is a prime number or not: '))
r = 0
for c in range(2, 90000000000000000000000000000000000000000000000000000):
    r = number / c
    if r < c:
        print(c)
        break
    r = number % c
    if r == 0:
        print(c)
        break
print(r)
if r == 0:
    print('This number is not prime')
if r != 0:
    print('This number is prime')
