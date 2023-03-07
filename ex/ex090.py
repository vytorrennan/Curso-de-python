student = dict()
student['name'] = input('Name: ').strip()
student['average'] = float(input(f'Average of {student["name"]}: '))
student['situation'] = 'Approved' if student['average'] >= 7 else 'Failed'
print(f'-=' * 24)
for k, v in student.items():
    print(f'  - The {k} is equal to {v}')
