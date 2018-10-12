import requests
from bs4 import BeautifulSoup
import csv

print('Now starting the web scrapper')

webLink = "https://www.census.gov/programs-surveys/popest.html"
webPage = requests.get(webLink)

if (webPage.status_code == 200):
    print('Successful conncection to web page')

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

print('Now printing to CSV file')
file = open('webLinkFile.csv', 'w')
with file:
    writer = csv.writer(file,lineterminator = '\n')
    for link in correctLinks:
        writer.writerow([link])

print("Links extracted")
