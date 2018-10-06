import requests
from bs4 import BeautifulSoup, SoupStrainer


#extract web links
webLink = "https://www.census.gov/programs-surveys/popest.html"
webPage = requests.get(webLink)

rawHtml = webPage.text

soup = BeautifulSoup(rawHtml, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))

#cast to absolute URIs

#verifies no duplicates

#save to CSV file
