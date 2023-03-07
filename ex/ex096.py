def area(width, height):
    print(f'The area of a terrain {width}x{height} is {width * height}m²')


print(' Terrain Control')
print('-' * 15)
w = float(input('Enter the width (m): '))
h = float(input('Enter the height (m): '))
area(w, h)
