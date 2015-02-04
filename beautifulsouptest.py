from bs4 import BeautifulSoup
import urllib2

url = "http://www.covers.com/pageLoader/pageLoader.aspx?page=/data/nba/matchups/g5_summary_11.html"

page = urllib2.urlopen(url).read()
bs = BeautifulSoup(page)

"""
for th in soup.findAll('th')[2:]:
	print th.text

for td in soup.findAll('td')[2:]:
	print td.text

for tr in soup.findAll('tr')[2:]:
	print tr.text
"""

table = bs.find(lambda tag: tag.name == 'table' and tag.has_key('id') and tag['id']=="Table1")
rows = table.findAll(lambda tag: tag.name == 'tr')
