from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

df = pd.read_csv('moviesall.csv', dtype={"tconst": "string", "title": "string", "original_title": "string", 
    "year": int, "genre": "string", "duration": int, "country": "string", "language": "string", "director": "string", 
    "writer": "string", "description": "string", "avg_vote": float, "votes": int} )
ids = []
for i in df['tconst']:
    ids.append(i)

urls = []
for i in ids:
    url = 'https://www.imdb.com/title/' + i + '/'
    urls.append(url)
#print(urls)

imgurls = []

for u in urls:    
    html_page = requests.get(u)
    
    soup = BeautifulSoup(html_page.content, 'html.parser')

    #for item in soup.find_all('h1'):
        #title = item.text
        #year = re.search('\(([^)]+)', title).group(1)
        #title = title.split('(')[0]
        #years.append(year)
        #titles.append(titles)
        
    for item in soup.find_all('div', class_ = 'poster'):
        imgurls.append(item.img['src'])

    #for item in soup.find_all('div', class_ = "inline canwrap"):
        #descrips.append(item.span.text)

df['imageurls'] = imgurls
print(df.head)

df.to_csv('export.csv', header=True)