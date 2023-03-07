from random import randint
from time import sleep


print('=' * 61)
print(" " * 26 + "*HANGMAN*")
print('=' * 61)

hangman = [
    '''=====
|   |
|   
|  
|  
|''',
    '''=====
|   |
|   o
|  
|  
|''',
    '''=====
|   |
|   o
|   |
|  
|''',
    '''=====
|   |
|   o
|   |
|  / 
|''',
    '''=====
|   |
|   o
|   |
|  / \ 
|''',
    '''=====
|   |
|   o
|  /|
|  / \ 
|''',
    '''=====
|   |
|   o
|  /|\ 
|  / \ 
|'''
]

# all the words in the game
animalInsectsWords = ['ANT', 'AXOLOTL', 'BAT', 'BEAR', 'BEE', 'BIRD', 'BUFFALO', 'CATFISH', 'CHEETAH', 'CHICKEN',
                      'CICADA', 'CRAB', 'COW', 'COYOTE', 'CORAL', 'CROCODILE', 'DOG', 'DUCK', 'DOLPHIN', 'DONKEY',
                      'ELEPHANT', 'ELECTRIC EEL', 'FROG', 'FALCON', 'FISH', 'FISHER CAT', 'FOX', 'FLAMINGO', 'GORILLA',
                      'GIRAFFE', 'GOAT', 'GOOSE', 'HAMSTER', 'HUMAN', 'HORSE', 'HEDGEHOG', 'JAGUAR', 'LION', 'LEOPARD',
                      'MONKEY', 'MOTH', 'OCELOT', 'PIG', 'PIGEON', 'PUG', 'RABBIT', 'RAT', 'WOODPECKER']
indieGames = ['Disco Elysium', 'Among Us', 'Cuphead', 'Fall Guys', 'Hades', 'Untitled Goose Game', 'Telling Lies',
              'Hypnospace Outlaw', 'The Witness', 'Rocket League', 'Inside', 'Into the Breach', 'Oxenfree',
              'Hotline Miami', 'Stardew Valley', 'Gone Home', 'What Remains of Edith Finch', 'Dead Cells',
              'Undertale', 'Gunpoint', 'Celeste', 'Papers, Please', 'Night in the Woods', 'Kerbal Space Program']
movies80 = ['E.T. the Extra-Terrestrial', 'Return of the Jedi', 'The Empire Strikes Back', 'Batman',
            'Raiders of the Lost Ark', 'Ghostbusters', 'Beverly Hills Cop', 'Back to the Future',
            'Indiana Jones and the Last Crusade', 'Indiana Jones and the Temple of Doom']
objects = ['Desk', 'Chair', 'Book', 'Notebook', 'Pencil case', 'Backpack', 'Scissors', 'Compass', 'Pins', 'Clip',
           'Pencil', 'Pencil sharpener', 'Stapler', 'Calculator', 'Ballpoint', 'Highlighter', 'eraser', 'Scotch tape',
           'Paint', 'Palette', 'Paint brush', 'Protractor', 'Set square', 'Ruler', 'Glue', 'Beaker', 'Flask',
           'Test tube', 'Funnel', 'Binder', 'Computer', 'Paper', 'File holder', 'Map', 'Magnifying glass', 'Clock',
           'Blackboard', 'Globe']
allCategories = [animalInsectsWords, indieGames, movies80, objects]

while True:
    print(" " * 26 + 'Loading...')
    sleep(2)
    # Setting and stating the game
    category = ''
    while category != '0' and category != '1' and category != '2' and category != '3':
        category = input('Choose a category\n'
                         '0 - Animals and insects\n'
                         '1 - Indie games\n'
                         '2 - 80\'s movies\n'
                         '3 - Objects\n'
                         'Enter a number between 0 and 3: ')
    category = int(category)
    hangmanCounter = 0
    print(hangman[hangmanCounter])
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    word = allCategories[category][randint(0, len(allCategories[category]) - 1)].upper()
    moldReplace = word
    for c in range(0, len(alphabet)):
        moldReplace = moldReplace.replace(alphabet[c], '_')
    print(f'\n{moldReplace}')
    # The repetitive part of the game
    while True:
        player = input('Enter the latter: ').strip().upper()
        while player not in alphabet:
            player = input('What you entered is invalid or you have already entered this, try again: ').strip().upper()
        print('=' * 24)
        alphabet.remove(player)
        moldReplace = word
        for c in range(0, len(alphabet)):
            moldReplace = moldReplace.replace(alphabet[c], '_')
        if player not in moldReplace and moldReplace.find('_') != -1:
            hangmanCounter += 1
        print(hangman[hangmanCounter])
        print(f'\n{moldReplace}')
        if moldReplace.find('_') == -1:
            print('**YOU WON!**')
            break
        if hangmanCounter == 6:
            print(f'**YOU LOSE! THE WORD WAS **{word}**')
            break
    # Starting another game or not
    print("=" * 26)
    anotherRound = ''
    while anotherRound == '' or anotherRound[0] != 'Y' and anotherRound[0] != 'N':
        anotherRound = input('Another round? [Y/N] ').strip().upper()
    if anotherRound[0] == 'Y':
        print('\n\n' + '=' * 61)
        print(" " * 26 + "Let's Go!")
        print('=' * 61)
    elif anotherRound[0] == 'N':
        print('\nThanks for playing!')
        break
