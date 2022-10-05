with open('data/osrs_words_v2.txt', 'r') as f:
    items = f.read().splitlines()


#
# with open('data/osrs_words_raw.txt', 'w+') as f:
#     for item in items_cleaned:
#         item = item.replace('(', '')
#         item = item.replace(')', '')
#         item = item.replace('.', '')
#         item = item.replace('\'', '')
#         item = item.replace('"', '')
#         item = item.replace('-', '')
#         f.write(item + '\n')

with open('data/osrs_words_short_v2.txt', 'w+') as f:
    for item in items:
        item = item.replace(' ', '')
        item = item.lower()
        item = ''.join(sorted(item))
        f.write(item + '\n')

# with open('data/res_candidates.txt', 'w+') as f:
#     for item in items_cleaned:
#         item = item.replace('(', '')
#         item = item.replace(')', '')
#         item = item.replace('.', '')
#         item = item.replace('\'', '')
#         item = item.replace(' ', '')
#         item = item.replace('"', '')
#         item = item.replace('-', '')
#         item = item.lower()
#         item = ''.join(set(item))
#         item = ''.join(sorted(item))
#         f.write(item + '\n')
