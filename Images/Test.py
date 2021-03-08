from bs4 import BeautifulSoup
import requests

html_page = requests.get('https://www.imdb.com/title/tt0078806/')

soup = BeautifulSoup(html_page.content, 'html.parser')

for item in soup.find_all('div', class_ = 'poster'):
    #print(item['src'])
    #print(item)
    print(item.img['src'])