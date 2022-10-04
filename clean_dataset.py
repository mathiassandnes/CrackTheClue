# load data

with open('data/items.txt', 'r') as f:
    items = f.read().splitlines()

cleaned_items = []
for item in items:
    item = item.replace('(', '')
    item = item.replace(')', '')
    item = item.replace('.', '')
    item = item.replace('\'', '')
    item = item.replace('"', '')
    item = item.replace('-', '')
    cleaned_items.append(item)

cleaned_items = list(set(cleaned_items))
cleaned_items = sorted(cleaned_items)

with open('data/osrs_words.txt', 'w+') as f:
    for item in cleaned_items:
        f.write(item + '\n')
