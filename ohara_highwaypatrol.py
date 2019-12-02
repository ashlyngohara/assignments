#####Step 1: Import libraries!

import requests, mechanize
from bs4 import BeautifulSoup

#Run code/file every couple lines or so to make sure it works

url = 'https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=10/31/2017'

br = mechanize.Browser()
br.open(url)
html = br.response().read()
#Or, html = requests.get(TYPEURL).content

#STEP 3: Make soup!

soup = BeautifulSoup(html, "html.parser")

#Step 4: Dig through the html

main_table = soup.find('tbody', {'id': 'accidentOutput'})

print(main_table)
#Returns "none"