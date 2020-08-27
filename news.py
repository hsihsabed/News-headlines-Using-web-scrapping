from selenium import webdriver
from bs4 import BeautifulSoup as SOUP 
import re
import urllib.request
import requests as HTTP
import os
import cv2
def Say(y):
    import pyttsx3

    y = str(y)
    
    engine = pyttsx3.init()
    engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.say(y)
    engine.setProperty('rate',1)  #120 words per minute
    engine.setProperty('volume',1) 
    engine.runAndWait()


Say('getting news headlines')
urlhere = ('https://www.ndtv.com/top-stories')
response = HTTP.get(urlhere) 
data = response.text
soup = SOUP(data, "lxml")


file = open('MyFile.txt','w')
file.write('')
file.close()

file1 = open("MyFile.txt","a")
i=1

for title in soup.findAll('h2',attrs = {"class" : re.compile('nstory_header')}):
    print(title.string)
    if i<=7:
        title = title.string
            
        title = title.split()
        str1 = '+'
        title = str1.join(title)
        title = title.replace("+"," ")
        
        
        img = cv2.imread('b.jpg')
        font = cv2.FONT_HERSHEY_SIMPLEX
        img = cv2.putText(img,str(title),(10,100), font, 0.5,(255,255,255),1,cv2.LINE_AA)
        
        cv2.imshow('',img)

        
        file1.write(str(title)+'\n')
        Say(str(title))
        i+=1
    
    else:
        break
    cv2.destroyAllWindows()

file1.close()


