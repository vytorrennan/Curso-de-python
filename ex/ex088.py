from random import randint
from time import sleep

games = []
print(f'=+' * 9, 'MEGA-SEINE', '+=' * 9)
howMany = int(input('Enter how many games you want: '))
for manyGames in range(0, howMany):
    games.append(list())
    while len(games[manyGames]) < 6:
        game = randint(1, 60)
        if game not in games[manyGames]:
            games[manyGames].append(game)
    games[manyGames].sort()
print('=+' * 24)
for c in range(0, howMany):
    print(f'Game {c + 1}: {games[c]}')
    sleep(1)
print('=+' * 24)
