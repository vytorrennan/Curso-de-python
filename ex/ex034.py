salary = float(input('Enter your salary: R$'))
if salary > 1250:
    percent = salary + (salary * 10 / 100)
    print('Your salary now with a 10% increase will be R${:.2f}'.format(percent))
else:
    percent = salary + (salary * 15 / 100)
    print('Your salary now with a 15% increase will be R${:.2f}'.format(percent))  
