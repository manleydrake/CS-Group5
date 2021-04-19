from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

df = pd.read_csv('moviesall.csv', dtype={"tconst": "string", "title": "string", "original_title": "string", 
    "year": int, "genre": "string", "duration": int, "country": "string", "language": "string", "director": "string", 
    "writer": "string", "description": "string", "avg_vote": float, "votes": int} )
df = df.iloc[0:151]
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
primewatch = []

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

    for item in soup.find_all('div', class_ = "inline canwrap"):
        if item.span.text:
            descrips.append(item.span.text)
        else: 
            descrips.append("NA")
    for item in soup.find_all('div', class_ = "buybox buybox--default buybox--desktop"):
        primewatch.append(item.a['href'])

df['imageurls'] = imgurls
df['fulldescriptions'] = descrips
df['primewatch'] = primewatch
#print(df.head)

df.to_csv('fulldescprimelink150.csv', header=True)