# load data

with open('../osrs_words.txt', 'r') as f:
    items = f.read().splitlines()

cleaned_items = []
for item in items:
    item = item.replace('(', '')
    item = item.replace(')', '')
    item = item.replace('.', '')
    item = item.replace('\'', '')
    item = item.replace('"', '')
    item = item.replace('-', '')
    item = item.lower()
    cleaned_items.append(item)

cleaned_items = list(set(cleaned_items))
cleaned_items = sorted(cleaned_items)

with open('../osrs_words_v2.txt', 'w+') as f:
    for item in cleaned_items:
        f.write(item + '\n')
