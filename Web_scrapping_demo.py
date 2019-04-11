from bs4 import BeautifulSoup
import requests
import csv


f = open('Quotes_data_2.csv', 'w')
writer = csv.DictWriter(f, ['quotes', 'source'])
writer.writeheader()

data_quotes = []

for i in range(1,225):
    
    # To define soup object 
    url = "http://www.values.com/inspirational-quotes" + "?" + "page={0}".format(i) 
    response = requests.get(url)   # To create request 
    soup = BeautifulSoup(response.text, 'lxml')
    
    # To print the url name
    print("Processing {0}".format(url))
    
    # tag the div with is protfolio
    quote_tag = soup.find('div', attrs = {'id': 'portfolio'})

    if quote_tag is not None:
        for row in quote_tag.find_all('div', attrs = {'class': 'portfolio-image'}):
            quotes = {}
            #print(row.img)
            full_quote = row.img.get('alt') if row.img is not None else 'Quotation in not defined.'
            src_quote = row.img.get('src') if row.img is not None else 'Source is not defined.'
            #print(full_quote)
            quotes['quotes'] = full_quote[:full_quote.rfind('.') + 1] # .rfind returns the count of argumetment possittion in a given string
            quotes['source'] = src_quote
            #print(quotes)
            data_quotes.append(quotes)
            writer.writerow(quotes)
    else:
        pass 

f.close()


