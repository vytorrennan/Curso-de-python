count = s = 0

while True:
    number = int(input('Enter a integer [enter 999 to stop the program]: '))
    if number == 999:
        break
    count += 1
    s += number
print(f'You enter {count} numbers and the sum of theses numbers is {s}!')
