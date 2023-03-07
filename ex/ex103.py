def player(name, goals):
    if not name.isalpha():
        name = '<unknown>'
    if not goals.isnumeric():
        goals = '0'
    return f'The player {name} did {goals} goal(s) in the championship'


print(player(input('Player\'s name: ').strip(), input('Number of goals: ')))
