import yaml
from tqdm import tqdm

from src.transformations import transform_clue_text

with open('data/osrs_words_v2.txt', 'r') as f:
    raws = f.read().splitlines()

with open('data/osrs_words_short_v2.txt', 'r') as f:
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


def find_anagrams(text_, samples):
    anagrams = []

    for (raw1, short1) in zip(raws, shorts):
        text = text_
        if is_anagram(text, short1):
            text = remove_letters(text, short1)
            if 1 in samples:
                anagrams.append(raw1)
            for (raw2, short2) in zip(raws, shorts):
                if is_anagram(text, short2):
                    text = remove_letters(text, short2)
                    if 2 in samples:
                        anagrams.append([raw1, raw2])
                    for (raw3, short3) in zip(raws, shorts):
                        if is_anagram(text, short3):
                            text = remove_letters(text, short3)
                            if 3 in samples:
                                anagrams.append([raw1, raw2, raw3])

    # anagrams_cleaned = []
    # for i, anagram in enumerate(anagrams):
    #     if type(anagram) == list:
    #         anagram.sort()
    #
    #     if anagram not in anagrams_cleaned:
    #         anagrams_cleaned.append(anagram)

    return anagrams

if __name__ == '__main__':

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

    clue = transform_clue_text(clue)

    output = {}
    for i, row in tqdm(enumerate(clue)):
        row_text = row['original'][:18] + ' ' + row['original'][18:]
        index = f'Row {i + 1}'
        output[index] = {'Row Text': row_text, 'candidates': []}

        for key, value in row.items():
            row[key] = ''.join(sorted(value.lower()))
            anagrams = find_anagrams(row[key], [1, 3, 2])
            output[index]['candidates'].append({
                'logic': key.replace('_', ' '),
                'text': row[key],
                'anagram combinations': len(anagrams),
                'anagrams': anagrams
            })

    with open('anagrams.yaml', 'w') as file:
        yaml.dump(output, file, sort_keys=False)

