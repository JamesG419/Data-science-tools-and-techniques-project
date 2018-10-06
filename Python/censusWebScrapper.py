import requests
from bs4 import BeautifulSoup, SoupStrainer


#extract web links
webLink = "https://www.census.gov/programs-surveys/popest.html"
webPage = requests.get(webLink)

rawHtml = webPage.text

soup = BeautifulSoup(rawHtml, 'html.parser')

correctLinks = set()
for link in soup.find_all('a'):
    if(link.get('href') != None):
        cleanedLink = link.get('href')

        if (cleanedLink.startswith('/')):
            cleanedLink = webLink + cleanedLink

        cleanedLink = cleanedLink.rstrip('/')
        correctLinks.add(cleanedLink)

#cast to absolute URIs

print(correctLinks)
#verifies no duplicates

#save to CSV file
