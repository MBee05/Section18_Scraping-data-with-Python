import requests
from bs4 import BeautifulSoup

res= requests.get('https://news.ycombinator.com/news')
soup= BeautifulSoup(res.text, 'html.parser')
links= soup.select('.titleline')
votes= soup.select('.score')


def create_custom_hn(links,votes):
    hn=[]
    for idx, item in enumerate(links):
        title= links[idx].getText()
        # hn.append(title)
        # display title of the links
        href= links[idx].get('href', None)
        # 'none' as default in the 2nd param if broken link
        # hn.append(href)
        # [None, None, None, None, None..
        
        # if want to combine title+link
        hn.append({'title': title, 'link': href})
        
        # points=votes[idx].getText()
        # convert this into 'int' select story that heve more than 100 pts, then keep and append and replace the pts into empty string
        points=int(votes[idx].getText().replace('points', ''))
        print(points)
        # got the nub but still have the error
    return hn
# print(create_custom_hn(links,votes))
create_custom_hn(links,votes)






