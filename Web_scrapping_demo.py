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
    full_quote = row.img.get('alt')
    src_quote = row.img.get('src')
    quotes['quote'] = full_quote[:full_quote.rfind('.') + 1] # .rfind returns the count of argumetment possittion in a given string
    quotes['url'] = src_quote
    data_quotes.append(quotes)
    #print(quotes)

with open('Quotes_data.csv', 'w') as file:
    writer = csv.DictWriter(file, ['quote', 'url'])
    writer.writeheader()
    for quote in data_quotes:
         writer.writerow(quote)



