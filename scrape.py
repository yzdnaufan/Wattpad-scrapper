from cgi import print_arguments
from nis import cat
import requests
from bs4 import BeautifulSoup
from time import sleep

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

obj_ =[]


class url:
    def __init__(self, judul, id, kategori, url_ ):
        self.judul = judul
        self.id = id
        self.kategori = kategori
        self.url_ = url_
        

novelID = []
novel =[]
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
    
    
    
def ListingsData(cats):
    
    soup = BeautifulSoup(cats, 'html.parser')
    headlines = soup.find(class_='browse-content-container').find_all('a', attrs={"class": "title meta on-story-preview"})


    
    
    
    return print(headlines[80]) 
    

def Scrape(obj):
    
    url = 'https://www.wattpad.com/' + str()
    response = s.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    story_title = soup.find(class_='browse-content').find_all('title meta on-story-preview')
    for x in story_title:
        web_ = x.find('a').get('href')
        url1 = str(web_) +'?single=1'
        
        
        novel.append(obj.judul)     #judul novel/tulisan
        
        novelID.append(obj.id)      #ID wattpad novel/tulisan
        
        inti.append(toi_article.text)   #text yang diambil
        
        kategori.append(obj.kategori)    #kategori text/tulisan
        
    sleep(5)
        
    return novel, novelID, inti, kategori

        