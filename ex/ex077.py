words = ('words', 'compass', 'clique', 'dirt', 'glass', 'pray', 'play', 'ping', 'live', 'hard', 'robot', 'place')
vowels = ('a', 'e', 'i', 'o', 'u')

for c in range(0, len(words)):
    print(f'The vowels in {words[c].upper()} are:', end=' ')
    i = 0
    while i < 5:
        if words[c].find(vowels[i]) != -1:
            print(vowels[i].upper(), end=' ')
        i += 1
    print('')
