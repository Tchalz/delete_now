'''
import urllib.request as urllib
from bs4 import BeautifulSoup
import re  # regular expression(re)


opener = urllib.build_opener()
opener.adddheaders = [("users-agent", "mozilla/5.0")]

url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_Nigerian_films"
openurl = opener.open(url).read()

soup = BeautifulSoup(openurl, features="html.parser")
for link in soup.find_all("a", attrs={"href": re.compile("^/wiki")}):
    print(link)


import sys
import requests
import bs4
res = requests.get(
    "https://en.wikipedia.org/wiki/Avengers:_Endgame" + " " .join(sys.argv[1:]))
res.raise_for_status()
wiki = bs4.BeautifulSoup(res.text, "html.parser")
for i in wiki.select("p"):
    print(i.getText())
'''


# write a program to get movie name, year and brief summary of the top 10 random movies
from bs4 import BeautifulSoup
import requests
import random
def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    movies = soup.find_all("td", class_="titleColumn")
    random.shuffle(movies)
    return movies

def get_imd_movie_info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.span.contents[0]
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url


def get_imd_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    return soup.find("div", class_="summary_text").contents[0].strip()

def get_imd_movie_info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.span.contents[0]
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url

def imd_movie_picker():
    ctr = 0
    print("--------------------------------------------")
    for movie in get_imd_movies('http ://www.imdb.com/chart/top'):
        movie_title, movie_year, movie_url = get_imd_movie_info(movie)
        movie_summary = get_imd_summary(movie_url)
        print(movie_title, movie_year)
        print(movie_summary)
        print("--------------------------------------------")
        ctr=ctr+1
        if (ctr==10):
            break;
if __name__ == '__main__':
    imd_movie_picker()




'''
from bs4 import BeautifulSoup
import requests

handle = input('Input your account name on Twitter: ') 
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text,'lxml')

try:
    following_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--following'})
    following = following_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("{} is following {} people.".format(handle,following.get('data-count')))

except:
    print('Account name not found...')
#output; showing that account name not found
'''
'''
import requests
from lxml import html
url = 'http://www.state.gov/r/pa/ode/socialmedia/'
doc = html.fromstring(requests.get(url).text)
pinlinks = [a for a in doc.cssselect('a') if 'pinterest.com' in str(a.attrib.get('href'))]
print("The number of Pinterest accounts maintained by U.S. State Department embassies and missions:")
print(len(pinlinks))
'''
'''
from bs4 import BeautifulSoup
import requests
handle = input('Input your account name on Twitter: ') 
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text,'lxml')
try:
    follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of followers: {} ".format(followers.get('data-count')))
except:
    print('Account name not found...')
'''
'''
from bs4 import BeautifulSoup
import requests

handle = input('Input your account name on Twitter: ') 
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text,'lxml')

try:
    favorite_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--favorites'})
    favorite = favorite_box.find('a').find('span',{'class':'ProfileNav-value'})
    print("Number of post {}  liked are {}: ".format(handle,favorite.get('data-count')))

except:
    print('Account name not found...')
'''
'''
from bs4 import BeautifulSoup
import requests
handle = input('Input your account name on Twitter: ')
ctr = int(input('Input number of tweets to scrape: '))
res=requests.get('https://twitter.com/'+ handle)
bs=BeautifulSoup(res.content,'lxml')
all_tweets = bs.find_all('div',{'class':'tweet'})
if all_tweets:
  for tweet in all_tweets[:ctr]:
    context = tweet.find('div',{'class':'context'}).text.replace("\n"," ").strip()
    content = tweet.find('div',{'class':'content'})
    header = content.find('div',{'class':'stream-item-header'})
    user = header.find('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
    time = header.find('a',{'class':'tweet-timestamp js-permalink js-nav js-tooltip'}).find('span').text.replace("\n"," ").strip()
    message = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
    footer = content.find('div',{'class':'stream-item-footer'})
    stat = footer.find('div',{'class':'ProfileTweet-actionCountList u-hiddenVisually'}).text.replace("\n"," ").strip()
    if context:
      print(context)
    print(user,time)
    print(message)
    print(stat)
    print()
else:
    print("list is empty/account name not found.")
'''