# - *- coding: utf- 8 - *-

#Production by Famaxth
#Telegram - @por0vos1k


import config
import requests
from bs4 import BeautifulSoup


def parse():
    URL = config.url
    HEADERS = {
        'User-Agent': config.user_agent
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'item news')
    comps = []

    for item in items:
        comps.append({
            'text': item.find('div', class_ = 'titles').get_text(strip = True),
            'theme': item.find('div', class_ = 'info g-date item__info').get_text(strip = True),
        })

        for comp in comps:
            print(f'{comp["theme"]}\nСобытие: {comp["text"]}\n\n\n')

parse() 
