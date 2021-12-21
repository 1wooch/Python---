#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen
title=[]
f=open("x.txt",'w',encoding='UTF-8')


response=urlopen('https://extmovie.com/movietalk') 
soup = BeautifulSoup(response, 'html.parser')
#for anchor in soup.select("a.title_link"):
#for anchor in soup.find_all('div',data-pswp-uid_=True):
#for anchor in soup.find_all('div',data-pswp-uid_ = true):
#    print(anchor)
for anchor in soup.find_all("div",{"class":"title_area"}):#{"class":"title_link"}):
#find_all("div",{"class":"title_area"}):#.find_all("a",{"class":"title_link"}):
#p=soup.find_all("div",{"class":"title_area"}).find_all("a",{"class":"title_link"})
    #print(anchor.get_text())
    title.append(anchor.get_text())
#print(title)
#del title[0:len(title):2]
for i in title:
    print(i[8:-5])
    #data=i[7:-5]
    
    f.write(str(i[8:-5])+"\n")
    #f.write(i[8:-5]+"\n")

    #i.strip("\t")

