from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

df = pd.read_csv('moviesall.csv', dtype={"tconst": "string", "title": "string", "original_title": "string", 
    "year": int, "genre": "string", "duration": int, "country": "string", "language": "string", "director": "string", 
    "writer": "string", "description": "string", "avg_vote": float, "votes": int} )
df = df.iloc[4000:5000]
ids = []
for i in df['tconst']:
    ids.append(i)

urls = []
for i in ids:
    url = 'https://www.imdb.com/title/' + i + '/'
    urls.append(url)
#print(urls)

imgurls = []
descrips = []
watchlink = []

for u in urls:    
    html_page = requests.get(u)
    
    soup = BeautifulSoup(html_page.content, 'html.parser')
        
    for item in soup.find_all('div', class_ = 'poster'):
        imgurls.append(item.img['src'])

    if soup.find('div', class_ = "inline canwrap"):
        descrips.append(soup.find('div', class_ = "inline canwrap").span.text)
    else:
        descrips.append("NA")

    if soup.find('div', class_ = "buybox buybox--default buybox--desktop"):
        watchlink.append(soup.find('a', class_ = "tracked-offsite-link buybox__link")['href'])
    else:
        watchlink.append("NA")
            
df['imageurls'] = imgurls
df['fulldescriptions'] = descrips
df['linktowatch'] = watchlink

df.to_csv('fulldescwatchlink40005000.csv', header=True)