import numpy as np

text = [
    ['YPWAIETOAENRMHMGEN', 'MIVWDMKDTCBANGBFKW'],
    ['NQLLWQMIRLVFSDROTN', 'VKIIAAKIRLHADHESVG'],
    ['LINVADMCURYBOFEUAI', 'DRULRHTDEESEBREPYE'],
    ['VRBOOHHSDEWEAANANN', 'EERATOLITEJEPEPZFN'],
    ['ANHIITBICPATELTTMH', 'FEKETCHPMSNAFEWNQM'],
    ['SFTOAINWLXARKLANFE', 'NEWEDSANENTEGQLHUA'],
    ['OENIRSRONOFKGVEKAR', 'TLBGONGUWHILPAFNAS'],
    ['EHERESSOVEMDGJTCWS', 'RDMCORRODAPJNLSAWY'],
    ['TASEWNHEVGRANOKNOT', 'SHTOELHTICUTMLHOIO'],
    ['HRFRONLRATTATTIQAT', 'ANEUOASGNHSFALEHND'],
]


def get_index(letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet.index(letter)


# letter index to letter
def get_letter(index):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet[index]


for row in text:
    # for a_, b_ in zip(row[0], row[1][::-1]):
    #     a = get_index(a_)
    #     b = get_index(b_)
    #     print(get_letter((a + b) % 26), end='')
    # print()
    a, b = row
    a = [get_index(letter) for letter in a]
    b = [get_index(letter) for letter in b]
    a = a[-1]
    b = b[0]

    diff = (a) + (b)
    diff = diff % 26
    diff = get_letter(diff)
    print('a+b', diff)

    diff = (a) - (b)
    diff = diff % 26
    diff = get_letter(diff)
    print('a-b', diff)

    diff = (b) - (a)
    diff = diff % 26
    diff = get_letter(diff)
    print('b-a', diff)
    print()
    # for letter in a:
    #     if letter in b:
    #         print(letter, end='')
    #
    # print('\n Left:')
    # for letter in a:
    #     if letter not in b:
    #         print(letter, end='')
    #
    # print('\n Right:')
    # for letter in b:
    #     if letter not in a:
    #         print(letter, end='')
    # print('\n', a, b)
