from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')
# temperatura = soup.find('<img>'', class_="-text -bold -gray-dark-2 -font-55 _margin-l-15")
img = soup.find('img', alt=True)
print(img['alt'])
# print(temperatura)

# print(soup.prettify())