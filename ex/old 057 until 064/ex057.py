sex = ''
while sex != 'M' and sex != 'F':
    sex = input('Enter your sex[M/F]: ').upper()
    if sex != 'M' and sex != 'F':
        print('Enter a valid answer!')
print('END')
