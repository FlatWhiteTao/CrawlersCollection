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

def singlePost(fonts):

    payload = {'word': 'Gallery.F', 'fonts':fonts,'sizes':'40','fontcolor':'#000000','colors':'#FFFFFF'}
    response = requests.post(url, data=payload)
    content = response.content
    #print(response.text)
    #print(response.status_code, response.reason)

    soup = BeautifulSoup(response.text,'lxml')

    imgs = soup.find('div',class_='s2')

    for img in imgs:
    
        link = img.get('src')
        flink = url + link
        print(flink)

        content2 = urllib2.urlopen(flink).read()
        with open(u'artEnglish'+'/'+flink[-11:],'wb') as code:
            code.write(content2)

fontsList = []
# "[0-9a-z_A-Z_\s]+.ttf" use regex to filter out needed fonts from a large html option list
fontsListFile = open("fontsList.txt")
for line in fontsListFile.readlines():
    line = line.strip('\n')
    fontsList.append(line)


for font in fontsList:
    singlePost(font)


