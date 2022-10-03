from bs4 import BeautifulSoup
import requests

# Get the page
urls = ['https://oldschool.runescape.wiki/w/Category:Free-to-play_items?from=0',
        'https://oldschool.runescape.wiki/w/Category:Free-to-play_items?filefrom=1&pagefrom=Black+2h+sword&subcatfrom=1#mw-pages',
        'https://oldschool.runescape.wiki/w/Category:Free-to-play_items?filefrom=1&pagefrom=Bucket&subcatfrom=1#mw-pages',
        'https://oldschool.runescape.wiki/w/Category:Free-to-play_items?filefrom=1&pagefrom=Decorative+helm+%28gold%29&subcatfrom=1#mw-pages',
        'https://oldschool.runescape.wiki/w/Category:Free-to-play_items?filefrom=1&pagefrom=Goblin+mail&subcatfrom=1#mw-pages',
        'https://oldschool.runescape.wiki/w/Category:Free-to-play_items?filefrom=1&pagefrom=Jug+of+water&subcatfrom=1#mw-pages',
        'https://oldschool.runescape.wiki/w/Category:Free-to-play_items?filefrom=1&pagefrom=Pearl+fishing+rod&subcatfrom=1#mw-pages',
        'https://oldschool.runescape.wiki/w/Category:Free-to-play_items?filefrom=1&pagefrom=Rune+platelegs+%28Last+Man+Standing%29&subcatfrom=1#mw-pages',
        'https://oldschool.runescape.wiki/w/Category:Free-to-play_items?filefrom=1&pagefrom=Steel+dagger&subcatfrom=1#mw-pages',
        'https://oldschool.runescape.wiki/w/Category:Free-to-play_items?filefrom=1&pagefrom=Voice+potion&subcatfrom=1#mw-pages',
        ]

with open('items.txt', 'w') as f:
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        for div in soup.find_all('div', class_='mw-category mw-category-columns'):
            for a in div.find_all('a'):
                f.write(a['title'] + '\n')
