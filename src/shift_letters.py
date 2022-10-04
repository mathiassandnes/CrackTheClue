text = '''YPWAIETOAENRMHMGENMIVWDMKDTCBANGBFKWNQLLWQMIRLVFSDROTNVKIIAAKIRLHADHESVGLINVADMCURYBOFEUAIDRULRHTDEESEBREPYEVRBOOHHSDEWEAANANNEERATOLITEJEPEPZFNANHIITBICPATELTTMHFEKETCHPMSNAFEWNQMSFTOAINWLXARKLANFENEWEDSANENTEGQLHUAOENIRSRONOFKGVEKARTLBGONGUWHILPAFNASEHERESSOVEMDGJTCWSRDMCORRODAPJNLSAWYTASEWNHEVGRANOKNOTSHTOELHTICUTMLHOIOHRFRONLRATTATTIQATANEUOASGNHSFALEHND'''
pattern = 'v^v^^^v^^v^^vv^^^v^vv^vvvvvv^v^vvv^^^^^^v^vv^^^^'
# shift = [-1, 1, -1, 3, -1, 2, -1, 2, -2, 3, -1, 1, -2, 1, -6, 1, -1, 1, -3, 6, -1, 1, -1, 4]
constants = 'bcdfghjklmnpqrstvwxz'
vowels = 'aeiouy'

# text = text[:312] + 'v^v^^^v^^v^^vv^^^v^vv^vvvvvv^v^vvv^^^^^^v^vv^^^^'
#
# for i, letter in enumerate(text):
#     if i % 36 == 0:
#         print(end='\n')
#     print(letter, end='')

shift = [-1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 0, 2, 0, 2, 0, 2, -2, 0, 2, 0, 2, 2]
# exit()


# shift = [x * -1 for x in shift]
# print(shift)

def ceasar_cipher(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = ''
    for letter in text:
        cipher += alphabet[(alphabet.index(letter) + shift) % len(alphabet)]

    return cipher


if __name__ == '__main__':
    for i, letter in enumerate(text):
        if i % 7 == 0:
            print(end='\n')
        print(letter, end='')


    # for i in range(26):
    # shift = []
    # for char in pattern:
    #     if char == 'v':
    #         shift.append(-1)
    #     else:
    #         shift.append(1)

    # # text = 'HTICUTMLHOIOHRFRONLRATTATTIQATANEUOASGNHSFALEHND'
    # clue = [
    #     ['YPWAIETOAENRMHMGEN', 'MIVWDMKDTCBANGBFKW'],
    #     ['NQLLWQMIRLVFSDROTN', 'VKIIAAKIRLHADHESVG'],
    #     ['LINVADMCURYBOFEUAI', 'DRULRHTDEESEBREPYE'],
    #     ['VRBOOHHSDEWEAANANN', 'EERATOLITEJEPEPZFN'],
    #     ['ANHIITBICPATELTTMH', 'FEKETCHPMSNAFEWNQM'],
    #     ['SFTOAINWLXARKLANFE', 'NEWEDSANENTEGQLHUA'],
    #     ['OENIRSRONOFKGVEKAR', 'TLBGONGUWHILPAFNAS'],
    #     ['EHERESSOVEMDGJTCWS', 'RDMCORRODAPJNLSAWY'],
    #     ['TASEWNHEVGRANOKNOT', 'SHTOELHTICUTMLHOIO'],
    #     ['HRFRONLRATTATTIQAT', 'ANEUOASGNHSFALEHND']
    # ]
    # for row in clue:
    #     text = ''.join(row)
    #     text = text.lower()
    #     text = [ceasar_cipher(letter, shift_amount) for letter, shift_amount in zip(text, shift)]
    #     text = ''.join(text)
    #     print(text)

#
# text = text.lower()
# for i in range(26):
#     text_ = ceasar_cipher(text, i)
#     text_ = list(text_)
#
#     for j, letter in enumerate(text_):
#         if letter in constants:
#             text_[j] = 'v'
#         else:
#             text_[j] = '^'
#
#     text_ = ''.join(text_)
#
#     print(f' ---------- {i} ---------- ')
#     print(text_)
#     print(pattern in text_)
