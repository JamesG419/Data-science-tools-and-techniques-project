import requests

webPage = requests.get("https://www.census.gov/programs-surveys/popest.html")

print(webPage.status_code)

