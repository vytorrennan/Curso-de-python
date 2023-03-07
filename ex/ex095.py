players = []

# collecting the data
while True:
    print('_' * 34)
    player = {'name': input('name of the player: '),
              'goals': list(),
              'total': 0}
    for c in range(0, int(input(f'How many matches {player["name"]} played? '))):
        player['goals'].append(int(input(f'How many goals in the match {c + 1}? ')))
        player['total'] += player['goals'][c]
    players.append(player.copy())
    continue_ = ' '
    while continue_ == '' or continue_[0] != 'Y' and continue_[0] != 'N':
        continue_ = input('Do you wanna add one more player? [ENTER JUST "Y" OR "N"] ').strip().upper()
    if continue_[0] == 'N':
        break
# showing the data
print('-=' * 34)
print('code nome              goals             total')
print('_' * 61)
for c in range(0, len(players)):
    print("{:>4} {:18}{:18}{}".format(c, players[c]['name'], str(players[c]['goals']), players[c]['total']))
while True:
    print('_' * 61)
    code = int(input('Enter the code of the player you want to see the data [to stop enter 999]: '))
    if code == 999:
        break
    if 0 < code > len(players) - 1:
        print(f'ERROR! Do not exist player {code}! Try again')
        continue
    print(f'The player {players[code]["name"]} played {len(players[code]["goals"])} matches.')
    for c in range(0, len(players[code]["goals"])):
        print(f'    ==> In match {c + 1}, did {players[code]["goals"][c]} goals.')
    print(f'It was a total of {players[code]["total"]} goals')
print('<< COME BACK LATER >>')
