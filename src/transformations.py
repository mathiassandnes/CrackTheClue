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
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet.upper()


def transform_clue_text(text):
    transformed_text = []
    for row in text:
        left = row[0]
        right = row[1]

        transformed_row = {
            'original': left + right,
            'both': ''.join([letter for letter in left if letter in right]),
            'left': ''.join([letter for letter in left if letter not in right]),
            'right': ''.join([letter for letter in right if letter not in left])
        }
        transformed_row['missing_original'] = ''.join(
            [letter for letter in alphabet if letter not in transformed_row['original']])
        transformed_row['missing_both'] = ''.join(
            [letter for letter in alphabet if letter not in transformed_row['both']])
        transformed_row['missing_left'] = ''.join(
            [letter for letter in alphabet if letter not in transformed_row['left']])
        transformed_row['missing_right'] = ''.join(
            [letter for letter in alphabet if letter not in transformed_row['right']])

        transformed_text.append(transformed_row)

    return transformed_text


if __name__ == '__main__':
    clue = transform_clue_text(clue)
    print(clue)
