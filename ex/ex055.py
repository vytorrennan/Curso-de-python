n = [0, 0, 0, 0, 0]
for c in range(1, 6):
    weight = float(input(f'Enter the {c}ª weight: '))
    n[c - 1] = weight
n.sort()
print(f'{n[4]:.1f}Kg was the heaviest')
print(f'{n[0]:.1f}Kg was the lightest')

'''
lista= []
for c in range (1,6):
    lista.append(float(input ('Qual o peso da {}ª pessoa? ' .format (c))))
print ('O maior peso é', max(lista))
print ('O menor peso é', min(lista))
'''