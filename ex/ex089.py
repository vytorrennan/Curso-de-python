allClass = []
student = []
continue_ = 'Y'

while continue_[0] == 'Y':
    student = [input('Name: '), [float(input('Grade 1: '))], [float(input('Grade 2: '))]]
    allClass.append(student[:])
    student.clear()
    continue_ = input('do you wanna to continue? [Y / N] ').upper().strip()

print('=+' * 40)
print(f'No. {"NAME":<15}average')
print('-' * 29)
for c in range(0, len(allClass)):
    print(f'{c}   {allClass[c][0]:<15}{(allClass[c][1][0] + allClass[c][2][0]) / 2:.1f}')
print('-' * 40)

while True:
    whichStudent = int(input('Enter the number of the student that you wanna see the grades [999 ends]: '))
    if whichStudent == 999:
        print('Thanks for using! finished')
        break
    print(f'The grades of {allClass[whichStudent][0]} are {allClass[whichStudent][1] + allClass[whichStudent][2]}')
