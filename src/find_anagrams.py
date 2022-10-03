import itertools
from tqdm import tqdm

with open('../data/res_raw.txt', 'r') as f:
    items = f.read().splitlines()

with open('../data/res_candidates.txt', 'r') as f:
    candidates = f.read().splitlines()

with open('../data/res_short.txt', 'r') as f:
    words = f.read().splitlines()


def get_combinations(text, mode='candidates', max_length=17):
    text = text.lower()
    if mode == 'candidates':
        text = ''.join(set(text))
        text = ''.join(sorted(text))
    combinations_list = []
    for i in range(2, max_length):
        combinations = itertools.combinations(text, i)
        combinations = [''.join(i) for i in combinations]
        combinations_list.extend(combinations)
    return combinations_list


def find_anagrams(text, mode='candidates'):
    text_sorted = ''.join(sorted(text))
    anagrams = get_combinations(text, mode=mode)
    candidates_list = []
    for anagram in tqdm(anagrams):
        matches = []
        for item, candidate, word in zip(items, candidates, words):
            if anagram == candidate:

                candidates_list.append((item, candidate, word))
                break

    return candidates_list


if __name__ == '__main__':
    candidates = find_anagrams('NNHTCTFPMFWNQMThessaliaTNW')
    # matches = find_anagrams('NANHTBCATFHPMFWNQMTNW', mode='matches')
    matches = sorted(candidates)
    print(*matches, sep='\n')

# TODO

# Find combinations of anagrams
# Search for items, locations and npcs

# Find candidates for text
# Use candidate to search for "words" candidates
