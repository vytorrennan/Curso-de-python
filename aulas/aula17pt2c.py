guys = list()
data = list()
totalGreatest = totalSmallest = 0

for c in range(0, 3):
    data.append(input('Name: '))
    data.append(int(input('Age: ')))
    guys.append(data[:])
    data.clear()

for person in guys:
    if person[1] >= 21:
        print(f'{person[0]} is more than 21 years old')
        totalGreatest += 1
    else:
        print(f'{person[0]} is less than 21 years old')
        totalSmallest += 1

print(f'We have {totalGreatest} people that are greater than 21 years old')
print(f'We have {totalSmallest} people that are smaller than 21 years old')
