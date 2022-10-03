import itertools

text = 'AAKIRLHADHESVGLINVADMCURYBOFEUAIDRULRHTDEESEBREPYEVRBOOHHSDEWEAANANNEERATOLITEJEPEPZFNANH'

# remove letters from text

words = ['Beer', 'Tuna', 'Pot', 'Wool', 'Potato', 'Vial', 'Coal', 'Coif']

# get all combinations of words
combinations = []
for i in range(2, len(words)):
    combs = itertools.combinations(words, i)
    combs = [''.join(i) for i in combs]
    combinations.extend(combs)

for word in combinations:
    word = word.lower()
    text_copy = text.lower()
    found = True
    for letter in word:
        if letter in text_copy:
            text_copy = text_copy.replace(letter, '', 1)
        else:
            found = False
            break
    if found:
        print(word)

text = text.replace('A', '')
