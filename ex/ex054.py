from datetime import date

more21 = 0
less21 = 0
for c in range(1, 8):
    bornYear = int(input(f'Enter the born year of the {c}ª person: '))
    if date.today().year - bornYear >= 21:
        more21 += 1
    if date.today().year - bornYear < 21:
        less21 += 1
print(f'{less21} of these persons has less then 21 years')
print(f'{more21} of these persons has more then 21 years')
