with open('../fishing', 'r') as f:
    items = f.read().splitlines()

items_cleaned = []
for item in items:
    if any(char.isdigit() for char in item):
        continue
    if '(' in item:
        continue
    if "'" in item:
        continue

    items_cleaned.append(item)

with open('../data/res_raw.txt', 'w+') as f:
    for item in items_cleaned:
        item = item.replace('"', '')
        item = item.replace('-', '')
        f.write(item + '\n')

with open('../data/res_short.txt', 'w+') as f:
    for item in items_cleaned:
        item = item.replace(' ', '')
        item = item.replace('"', '')
        item = item.replace('-', '')
        item = item.lower()
        item = ''.join(sorted(item))
        f.write(item + '\n')

with open('../data/res_candidates.txt', 'w+') as f:
    for item in items_cleaned:
        item = item.replace(' ', '')
        item = item.replace('"', '')
        item = item.replace('-', '')
        item = item.lower()
        item = ''.join(set(item))
        item = ''.join(sorted(item))
        f.write(item + '\n')
