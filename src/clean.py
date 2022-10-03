with open('data/f2p-npcs-items.csv', 'r') as f:
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

with open('data/res_cleaned.txt', 'w') as f:
    for item in items_cleaned:
        item = item.replace('"', '')
        item = item.replace('-', '')
        f.write(item + '\n')

with open('data/res_transformed.txt', 'w') as f:
    for item in items_cleaned:
        item = item.replace(' ', '')
        item = item.lower()
        item = ''.join(set(item))
        item = ''.join(sorted(item))
        f.write(item + '\n')
