# Send a POST request to an online art word converting tool and then
# crawl the converted pic and save into the local folder "artEnglish"

from selenium import webdriver
import requests
import json
from bs4 import BeautifulSoup
import os,sys,urllib2

path = os.getcwd()
new_path = os.path.join(path,u'artEnglish')
if not os.path.isdir(new_path):
    os.mkdir(new_path)

url = "http://www.popzitizh.com/yw/"

payload = {'word': 'Gallery.F', 'fonts':'Cyberfunk.ttf','sizes':'40','fontcolor':'#000000','colors':'#FFFFFF'}
response = requests.post(url, data=payload)
content = response.content
print(response.text)
print(response.status_code, response.reason)

soup = BeautifulSoup(response.text,'lxml')

imgs = soup.find('div',class_='s2')

for img in imgs:
    
        link = img.get('src')
        flink = url + link
        print(flink)

        content2 = urllib2.urlopen(flink).read()
        with open(u'artEnglish'+'/'+flink[-11:],'wb') as code:
            code.write(content2)




