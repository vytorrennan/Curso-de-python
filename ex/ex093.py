player = {'name': input('name of the player: '),
          'goals': list(),
          'total': 0}
for c in range(0, int(input(f'How many matches {player["name"]} played? '))):
    player['goals'].append(int(input(f'How many goals in the match {c + 1}? ')))
    player['total'] += player['goals'][c]
print('-=' * 60)
print(player)
print('-=' * 60)
for k, v in player.items():
    print(f'{k} have value {v}.')
print('-=' * 60)
print(f'The player {player["name"]} played {len(player["goals"])} matches.')
for c in range(0, len(player['goals'])):
    print(f'    ==> In match {c + 1}, did {player["goals"][c]} goals.')
print(f'It was a total of {player["total"]} goals')
