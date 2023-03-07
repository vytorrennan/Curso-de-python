# taking the person's data
weight = float(input('What\'s your weight? '))
height = float(input('What\'s your height? '))
# calculation of body mass index
IMC = weight / (height * height)
print(f'Your body mass index is {IMC:.1f}')
if IMC < 18.5:
    print('{}Underweight{}'.format('\033[35m', '\033[m'))
elif 18.5 < IMC < 25:
    print('{}Ideal weight{}'.format('\033[32m', '\033[m'))
elif 25 < IMC < 30:
    print('{}Over weight{}'.format('\033[34m', '\033[m'))
elif 30 < IMC < 40:
    print('{}Obesity{}'.format('\033[33m', '\033[m'))
elif IMC > 40:
    print('{}Morbid obesity{}'.format('\033[31m', '\033[m'))
