from asyncio.windows_events import NULL
import requests
from bs4 import BeautifulSoup
from time import sleep

import random

import os
import time


def seed( s=100 ) :
    random.seed(s)
    
class url:
    def __init__(self, judul, id, kategori, url_ ):
        self.judul = judul
        self.id = id
        self.kategori = kategori
        self.url_ = url_
        


novelID = []
judul =[]
inti = []
kategori = []

link = 'https://www.wattpad.com/login'

with requests.Session() as s:
    s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    res = s.get(link)
    soup = BeautifulSoup(res.text,'html.parser')   
    payload = {i['name']:i.get('value','') for i in soup.select('input[name]')}         
    #what the above line does is parse the keys and valuse available in the login form
    payload['username'] = 'dscnl001'
    payload['password'] = '1234qwer'

    print(payload) #when you print this, you should see the required parameters within payload 

    s.post(link,data=payload)
    
    
    
def ListingsData(cats, i):
    '''
    Returning object list with attributes :
    :judul:
    :id:
    :kategori:
    :url_:
    '''
    
    obj_ =[]
    with open('html/' +str(cats)+ '.html', 'r', encoding='utf-8') as o :
        soup = BeautifulSoup(o, 'html.parser')
        headlines = soup.find(class_='browse-content-container').find_all('a', attrs={"class": "title meta on-story-preview"})
        
        for int in range(i):
            Url = url(headlines[int].text, headlines[int].get('data-story-id'), cats, 'https://wattpad.com'+ headlines[int].get('href'))
            obj_.append(Url)
        
    
    return obj_

def Scrape(obj):
    
    
    url = obj.url_
    
    #Novel Openner
    response = s.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if soup.find(class_='story-parts') is None:
        judul.append(obj.judul)         #judul novel/tulisan
    
        novelID.append(obj.id)          #ID wattpad novel/tulisan
    
        inti.append(None)             #text yang diambil
    
        kategori.append(obj.kategori)
        
        return judul, novelID, inti, kategori
    
    
    novel = soup.find(class_='story-parts').find_all('li')
    
    #random chapter pick
    chapter = novel[random.randint(0, len(novel)-1)]
    
    
    #locked chapter mitigation
    #while chapter.find('title') is not None :
    #    i = random.randint(0, len(novel)-1)
    #    chapter = novel[i]
    
    #Chapter Opener
    url = 'https://wattpad.com'+ str(chapter.find('a').get('href'))
    response = s.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    
    
    text = soup.find(class_ = 'story-part').find_all('p')
    
    #get text paragraph randomized
    p = text[random.randint(0, len(text)-1)]
    
    #unwanted text mitigation (e.g. Episode Text etc.)
    #while p.get('style') is not None :
    #    i = random.randint(0, len(text)-1)
    #    p = text[i]
        
    
    judul.append(obj.judul)         #judul novel/tulisan
    
    novelID.append(obj.id)          #ID wattpad novel/tulisan
    
    inti.append(p.text)             #text yang diambil
    
    kategori.append(obj.kategori)    #kategori text/tulisan
    
    sleep(5)
    
    return judul, novelID, inti, kategori

        