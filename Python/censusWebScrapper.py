import requests
from bs4 import BeautifulSoup
import csv



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

correctLinks = list(correctLinks)

file = open('webLinkFile.csv', 'w')
with file:
    writer = csv.writer(file,lineterminator = '\n')
    for link in correctLinks:
        writer.writerow([link])

print("Links extracted")
