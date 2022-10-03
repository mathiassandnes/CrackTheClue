import itertools
from tqdm import tqdm

with open('items_cleaned.txt', 'r') as f:
    items = f.read().splitlines()

with open('items_cleaned_v2.txt', 'r') as f:
    items2 = f.read().splitlines()


def get_combinations(text, max_length=17):
    text = text.lower()
    text = ''.join(set(text))
    print('Generationg combinations...')
    combinations_list = []
    for i in range(2, max_length):
        combinations = itertools.combinations(text, i)
        combinations = [''.join(i) for i in combinations]
        for combination in combinations:
            combinations_list.append(combination)

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
    res =  [i for i in zip(items, items2) if len(i[1]) == length]
    print(res)
    return res


def find_anagrams(text):
    # with open('anagrams.txt', 'a') as f:
    combinations = get_combinations(text)
    matches = []
    for combination in combinations:
        for value, value2 in get_items_with_length(len(combination)):
            if combination == value2:
                matches.append(value)
                # f.write(f'{value} - {combination} \n')
                break
    return matches


if __name__ == '__main__':
    find_anagrams('poultry outwits ants')
