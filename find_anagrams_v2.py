with open('data/res_raw.txt', 'r') as f:
    raws = f.read().splitlines()

with open('data/res_short.txt', 'r') as f:
    shorts = f.read().splitlines()


def is_anagram(anagram, candidate):
    if len(anagram) == 0 or len(anagram) < len(candidate):
        return
    remainder = anagram
    for letter in candidate:
        if letter in remainder:
            remainder = remainder.replace(letter, '', 1)
        else:
            return False
    return True


def remove_letters(text, letters):
    for letter in letters:
        text = text.replace(letter, '', 1)
    return text


def find_anagrams(text_):
    anagrams = []

    for (raw1, short1) in zip(raws, shorts):
        text = text_
        if is_anagram(text, short1):
            text = remove_letters(text, short1)
            anagrams.append(raw1)

            for (raw2, short2) in zip(raws, shorts):
                if is_anagram(text, short2):
                    text = remove_letters(text, short2)
                    anagrams.append([raw1, raw2])

                    for (raw3, short3) in zip(raws, shorts):
                        if is_anagram(text, short3):
                            text = remove_letters(text, short3)
                            anagrams.append([raw1, raw2, raw3])

    return anagrams


clue = [
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

for row in clue:
    for i, col_ in enumerate(row):
        col = col_.lower()
        col = ''.join(sorted(col))
        anagrams = find_anagrams(col)
        print(col_, anagrams)
