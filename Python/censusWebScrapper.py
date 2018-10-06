import requests
from bs4 import BeautifulSoup, SoupStrainer

webPage = requests.get("https://www.census.gov/programs-surveys/popest.html")

rawHtml = webPage.text

soup = BeautifulSoup(rawHtml, 'html.parser')

print(soup.prettify())
