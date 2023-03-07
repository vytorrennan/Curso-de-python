n = s = 0
while True:
    n = int(input('Enter a number: '))
    if n == 999:
        break
    s += n
print(f'adding theses numbers is {s}')
