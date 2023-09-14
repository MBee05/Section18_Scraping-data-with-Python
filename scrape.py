import requests
from bs4 import BeautifulSoup
# BeautifulSoup allows us to use html and grab different data to scrape it, Requests module allows to download that html


# could be web browser
res= requests.get('https://news.ycombinator.com/news')
# print(res)
# <Response [200]>

# print(res.text)
# display all the html txt so we grab this data
# now we want to use Beautif to clean up this data, remove info that we dont need

soup= BeautifulSoup(res.text, 'html.parser')
# print(soup)
# display the all html pg and we can grab what we need from it ex. if we want grab the body then have to print

# print(soup.body)
# display the body

# print(soup.body.contents)
# display the entire content

# print(soup.find_all('div'))
# display all the div obj in a list


# print(soup.find_all('a'))
# dsiplay all the 'a' tag


# print(soup.title)
# <title>Hacker News</title>

# print(soup.a)
# display the 1st 'a' tag from the html


# print(soup.find('a'))
# display the 1st 'a' tag from the html

# why useful, inspect the pg and can check the tag that you are interested in 
# ex the point so 'id' attribute

# print(soup.find(id="score_37272652"))
# <span class="score" id="score_37272652">292 points</span>


# print(soup.select('a'))
# this way it helps us to grab data through a css selector
# display the 'a' tag

# print(soup.select('.score'))
# display all the score from that html pg

# print(soup.select('#score_37272652'))
# [<span class="score" id="score_37272652">300 points</span>]



# we want to select only the stories that are more than 100 points and filter the rest

# print(soup.select('.titleline'))
# grabs all the titleline


# print(soup.select('.titleline')[0])
# display only the first story

# grab all the links
links= soup.select('.titleline')


# grab all the score
votes= soup.select('.score')
# print(votes[0])
# grab the first item   
# <span class="score" id="score_37274871">28 points</span>


# get for ex an attribute name
# print(votes[0].get('id'))
# # score_37274871
