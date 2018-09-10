import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.passiton.com/inspirational-quotes"
res = requests.get(url)

soup = BeautifulSoup(res.content,'html5lib')

table = soup.find('div',attrs = {'id':'portfolio'})

quotes = []

for row in table.findAll('article'):
    quote = {}
    quote['theme'] = row['class'][2]
    quote['link'] = row.div.a['href']
    quote['lines'] = row.div.a.img['alt']
    quote['image'] = row.div.a.img['src']
    quotes.append(quote)

filename = 'inspirational_quotes.csv'

with open(filename,'w') as f:
    w = csv.DictWriter(f,fieldnames = ['theme','link','lines','image'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

