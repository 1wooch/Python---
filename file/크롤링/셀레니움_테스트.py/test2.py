from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 
import csv
#from find_text import check_string
from selenium.common.exceptions import NoSuchElementException

f=open("소진지점.txt",'w',encoding='UTF-8')

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://extmovie.com/movietalk/71696227')
driver.implicitly_wait(5)
소진지점=[]




CGV서울=[]
CGV경기=[]
CGV인천=[]
CGV충남=[]
CGV대구=[]
CGV전남=[]
CGV강원=[]
CGV부산=[]
CGV=[]
MegaBox=[]
LotteCinema=[]

소진지점2=['등촌','용산','영등포','왕십리','목동','센텀']
서울소진=[]
with open('cgv.txt','r',encoding='UTF-8') as fd:
    reader=csv.reader(fd)
    for row in reader:
        CGV.append(row)
print(CGV)
CGV서울.extend(CGV[0])
CGV경기.extend(CGV[1])
CGV인천.extend(CGV[2])
CGV충남.extend(CGV[3])
CGV대구.extend(CGV[4])
CGV전남.extend(CGV[5])
CGV강원.extend(CGV[6])
CGV부산.extend(CGV[7])

for s1 in CGV서울:
    for s2 in 소진지점2:
        if s1==s2:
            서울소진.append(s1)

print(서울소진)