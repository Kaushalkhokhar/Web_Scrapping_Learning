import requests
import bs4

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# reqs = requests.get('https://learncodeonline.in')
soup = bs4.BeautifulSoup(html_doc, 'lxml')

"""# To find the link of websites
for link in soup.findAll('a'):
    print(link.get('href'))"""

"""fing_a = soup.findAll('a')
print(fing_a"""

"""for tag in soup.findAll('a'):
    print(tag.attrs)
    print(tag.string)
"""
print(len(list(soup.descendants)))
print(len(list(soup.children)))

"""# To find the tags:
for tag in soup.descendants:
    if tag.name is None:
        pass
    else:
        print(tag.name)"""

"""for child in soup.children:
    print(child.name)"""

# To print siblings
for siblings in soup.head.next_siblings:
    print(siblings.name)
