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
input = raw_input("please input the word you want to convert:")
#input = 'Gallery.F'

def singlePost(fonts):
    
    uniqueOutPath = os.path.join(new_path,input)
    if not os.path.isdir(uniqueOutPath):
        os.mkdir(uniqueOutPath)

    payload = {'word': input, 'fonts':fonts,'sizes':'40','fontcolor':'#000000','colors':'#FFFFFF'}
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
        with open(u'artEnglish'+'/'+input+'/'+flink[-11:],'wb') as code:
            code.write(content2)

fontsList = []
# "[0-9a-z_A-Z_\s]+.ttf" use regex to filter out needed fonts from a large html option list
fontsListFile = open("fontsList.txt")
for line in fontsListFile.readlines():
    line = line.strip('\n')
    fontsList.append(line)


for font in fontsList:
    singlePost(font)


