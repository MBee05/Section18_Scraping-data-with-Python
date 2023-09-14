import requests
from bs4 import BeautifulSoup
import pprint

res= requests.get('https://news.ycombinator.com/news')
soup= BeautifulSoup(res.text, 'html.parser')
links= soup.select('.titleline')
subtext= soup.select('.subtext')


def create_custom_hn(links,subtext):
    hn=[]
    for idx, item in enumerate(links):
        # we enumerate over the links and subtext is enumerated. We need the idx so that we have access this subtext within our loops otherwise if we didnt enumerate, cant grab both links and subtext so we can convert links into 'item'
        # title= links[idx].getText()
        title= item.getText()
        href= item.get('href', None)
        vote=subtext[idx].select('.score')
        if len(vote):
            points=int(vote[0].getText().replace('points', ''))
            if points > 99:
            # print(points)
                hn.append({'title': title, 'link': href,'votes': points})
        # got the nub but still have the error
    return hn
pprint.pprint(create_custom_hn(links,subtext))
# create_custom_hn(links,subtext)






