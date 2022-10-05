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

        t_row = {
            'original': left + right,
            'left': left,
            'right': right,
            'both': ''.join([letter for letter in left if letter in right]),
            'left_only': ''.join([letter for letter in left if letter not in right]),
            'right_only': ''.join([letter for letter in right if letter not in left]),
            'left_with_right_letters_subtracted': list(left),
            'right_with_left_letters_subtracted': list(right),
        }

        for letter in right:
            if letter in t_row['left_with_right_letters_subtracted']:
                t_row['left_with_right_letters_subtracted'].remove(letter)
        t_row['left_with_right_letters_subtracted'] = ''.join(t_row['left_with_right_letters_subtracted'])

        for letter in left:
            if letter in t_row['right_with_left_letters_subtracted']:
                t_row['right_with_left_letters_subtracted'].remove(letter)
        t_row['right_with_left_letters_subtracted'] = ''.join(t_row['right_with_left_letters_subtracted'])

        t_row_copy = t_row.copy()
        for key in t_row_copy.keys():
            t_row[f'missing_{key}'] = ''.join([letter for letter in alphabet if letter not in t_row[key]])
        transformed_text.append(t_row)

    return transformed_text


if __name__ == '__main__':
    clue = transform_clue_text(clue)
    print(clue)
