import requests
from bs4 import BeautifulSoup

url = 'https://www.brewersfriend.com/search/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

soup.find("table", {'class':'recipeitems'})

data = []
for tr in soup.find("table", {'class':'recipeitems'}):
    cols = tr.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    
print(data)arquivo