import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

matplotlib.use('TkAgg')

# clue = '''YPWAIETOAENRMHMGENMIVWDMKDTCBANGBFKWNQLLWQMIRLVFSDROTNVKIIAAKIRLHADHESVGLINVADMCURYBOFEUAIDRULRHTDEESEBREPYEVRBOOHHSDEWEAANANNEERATOLITEJEPEPZFNANHIITBICPATELTTMHFEKETCHPMSNAFEWNQMSFTOAINWLXARKLANFENEWEDSANENTEGQLHUAOENIRSRONOFKGVEKARTLBGONGUWHILPAFNASEHERESSOVEMDGJTCWSRDMCORRODAPJNLSAWYTASEWNHEVGRANOKNOTSHTOELHTICUTMLHOIOHRFRONLRATTATTIQATANEUOASGNHSFALEHND'''
# text = 'AAKIRLHADHESVGLINVADMCURYBOFEUAIDRULRHTDEESEBREPYEVRBOOHHSDEWEAANANNEERATOLITEJEPEPZFNANH'
text = 'guhdvulminjpgqgspmmqzuszsshpbsbmdtpbthoirgzkfioe'

def remove_letters(text, letters):
    for letter in letters:
        text = text.replace(letter, '', 1)
    return text


text = remove_letters(text, 'alkharidwoolvialmithrilbar')


# get frequency of each letter
def get_frequency(text):
    frequency = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
                 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for letter in text:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency


frequency = get_frequency(text.lower())

# plot frequency in descending order
df = pd.DataFrame.from_dict(frequency, orient='index')
df.columns = ['frequency']
df = df.sort_values(by='frequency', ascending=False)
df.plot(kind='bar')
plt.show()
