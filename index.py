from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve, urlopen, Request
import os
import threading 

categories = [
    {
        'name': 'Cars',
        'path': 'car-logos'
    },
    {
        'name': 'Fashion',
        'path': 'fashionaccessories'
    },
    {
        'name': 'Internet',
        'path': 'internet-logos'
    },
    {
        'name': 'Soccer',
        'path': 'soccer'
    },
    {
        'name': 'Technology',
        'path': 'technology-logo'
    },
    {
        'name': 'Drinks',
        'path': 'drink-logos'
    },
    {
        'name': 'E-Commerce',
        'path': 'e-commerce'
    },
    {
        'name': 'Financial',
        'path': 'financualbank'
    },
    {
        'name': 'Media',
        'path': 'mediatv'
    },
    {
        'name': 'Industrial',
        'path': 'industrial'
    },
    {
        'name': 'Food',
        'path': 'food-logos'
    },
    {
        'name': 'Basketball',
        'path': 'basketball'
    }
]

baseurl = 'https://1000logos.net'

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'
}

def scrapeCategory(cat):
    global baseurl, session, headers 

    res = session.get(f"{baseurl}/{cat['path']}/", headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')

    # get the top 10
    top10Container = bs.find('aside', {'class': 'widget sidebar-widget popular-posts'})
    top10 = top10Container.find('ul', {'class': 'wpp-list-with-thumbnails'}).children
    cat['top10'] = []
    for li in top10:
        name = li.text.strip()
        link = li.find('a', {'class': 'wpp-post-title'}).attrs['href']
        cat['top10'].append({
            'name': name,
            'url': link
        })

    # download the image
    for link in cat['top10']:
        res = session.get(link['url'], headers=headers)
        bs = BeautifulSoup(res.text, 'html.parser')
        p = bs.find('p', {'style': 'text-align: center;'})
        imagePath = p.find('a').attrs['href']
        print(imagePath)
        req = requests.get(imagePath)
        with open(f"images/{cat['name']}/{link['name']}.png", 'wb') as f:
            f.write(req.content)

threads = []

for cat in categories:
    thread = threading.Thread(target=scrapeCategory, args=(cat,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()