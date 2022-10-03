import itertools
from tqdm import tqdm

with open('data/res_cleaned.txt', 'r') as f:
    items = f.read().splitlines()

with open('data/res_transformed.txt', 'r') as f:
    items2 = f.read().splitlines()


def get_combinations(text, max_length=17):
    text = text.lower()
    text = ''.join(set(text))
    text = ''.join(sorted(text))
    combinations_list = []
    for i in range(2, max_length):
        combinations = itertools.combinations(text, i)
        combinations = [''.join(i) for i in combinations]
        combinations_list.extend(combinations)
    return combinations_list


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def get_items_with_length(length):
    res = [i for i in zip(items, items2) if len(i[1]) == length]
    return res


def find_anagrams(text):
    # with open('anagrams.txt', 'a') as f:
    combinations = get_combinations(text)
    matches = []
    for combination in combinations:
        # for value, value2 in get_items_with_length(len(combination)):
        for value, value2 in zip(items, items2):
            if combination == value2:
                matches.append(value)
                # f.write(f'{value} - {combination} \n')
                break
    return matches


if __name__ == '__main__':
    find_anagrams('poultry outwits ants')
