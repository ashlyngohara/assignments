######## STEP 1: Import your libraries! #####

import csv
import requests, mechanize
from bs4 import BeautifulSoup

csvfile = open('jail.csv,' 'a')
jail_writer = csv.writer(csvfile)

###### STEP 2: Get the HTML! ######

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'

br = mechanize.Browser()
br.open(url)
html = br.response().read()

soup = BeautifulSoup(html, "html.parser")

main_table - soup.find('tbody', {'id': 'mrc_main_table'})

row_list = main_table.find_all('tr')

	table_cells = row.find_all('td')

	for cell in table_cells:
		print(cell.text) 