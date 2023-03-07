var = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Internacional', 'Palmeiras', 'Santos', 'Grêmio', 'Fluminense',
       'Fortaleza', 'Corinthians', 'Ceará', 'Athletico-PR', 'Bahia', 'Atlético-GO', 'Bragantino', 'Sport', 'Vasco',
       'Coritiba', 'Botafogo', 'Goiás')
print(f'The rank of soccer teams in brazil: {var}\n{"-" * 34}')
print(f'The first 5 is: {var[0:5]}\n{"-" * 34}')
print(f'The lasted 4 is: {var[-4:]}\n{"-" * 34}')
print(f'In alphabetic order is: {sorted(var)}\n{"-" * 34}')
print(f'The Corinthians is in the {var.index("Corinthians") + 1}ª position')
