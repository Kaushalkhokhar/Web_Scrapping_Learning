import requests
import bs4
import csv

reqs = requests.get('http://www.values.com/inspirational-quotes')
soup = bs4.BeautifulSoup(reqs.text, 'lxml')

# print(soup.prettify())

'''img_tag = soup.find_all('div', class_ = ''):
    pass)
img_tag = list(img_tag)
print(img_tag[0])'''

quote_tag = soup.find('div', attrs = {'id': 'portfolio'})

#print(table.article.prettify())

data_quotes = []

for row in quote_tag.find_all('div', attrs = {'class': 'portfolio-image'}):
    quotes = {}
    quotes['quote'] = row.img.get('alt')
    quotes['url'] = row.img.get('src')
    data_quotes.append(quotes)
    #print(quotes)

with open('Quotes_data.csv', 'w') as file:
    writer = csv.DictWriter(file, ['quote', 'url'])
    writer.writeheader()
    for quote in data_quotes:
         writer.writerow(quote)



