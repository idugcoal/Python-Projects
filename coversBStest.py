from urllib2 import urlopen  # for Python 3: from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://sports.yahoo.com/nba/teams/lal/stats/"
soup = BeautifulSoup(urlopen(url))

label = soup.find(text = "Games")
games = label.string()
print games