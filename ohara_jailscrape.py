#Ashlyn O'Hara
#Chase Davis
#Advanced Data
#14 October 2019

#Documentation Assignment

import urllib2, csv
#Imports a file by identifying the title and the file type.

from bs4 import BeautifulSoup
#Imports the BeautifulSoup library and locates it within bs4.

outfile = open('jaildata.csv', 'w')
#Tells it to creat a file called jaildata.csv that we are going to write.

writer = csv.writer(outfile)
#Tells it to create/write a new csv file. 

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#Provides the location of the file on the web. 

html = urllib2.urlopen(url).read()
#Specifies that what we are scraping is html and tells it to to open the URL provided above. 

soup = BeautifulSoup(html, "html.parser")
#Accesses a command/term from Beautiful Soup" called "soup" that will parse the site's HTML.

tbody = soup.find('tbody', {'class': 'stripe'})
#Further specifies the soup command by telling it to find a 'tbody' attribute with 'class: stripe' characteristics in the HTML it just parsed. 

rows = tbody.find_all('tr')
#Once the 'tbody' is found, this tells it to locate all the rows containing 'tr'. T row? Table row? 

for row in rows:
#Tells is that for all the rows found by the rows command to do the following.

    cells = row.find_all('td')
#Tells that for a row found in rows to find all of the cells. 

    data = []
#Says that we will be performing data work of some kind on the results of our search in HTML. 

    for cell in cells:
#For all the cells found in our cell search: 

        data.append(cell.text.encode('utf-8'))
#Append the data by translating it to utf-8 encoded data. 

    writer.writerow(data)
#Tells it to actually create the data file using all the search parameters specified with the previous commands. 
