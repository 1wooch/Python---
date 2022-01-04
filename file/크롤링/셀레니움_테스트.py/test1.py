from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 
import csv
import telegram
#from find_text import check_string
f=open("소진지점.txt",'w',encoding='UTF-8')

토큰='5081033456:AAFC9HDCGCdGyvKe2inpuxkHfKSV7Ab1Rww'
봇 = telegram.Bot(token=토큰)

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://extmovie.com/movietalk/71696227')
driver.implicitly_wait(5)
소진지점=[] #before sorting
소진지점2=[] #after sorting by '소진' ,'끝'
테스트=""
CGV서울=[]
CGV경기=[]
CGV인천=[]
CGV충남=[]
CGV대구=[]
CGV전남=[]
CGV강원=[]
CGV부산=[]

CGV서울소진필름마크=[]
CGV서울소진아맥포스터=[]

CGV경기소진필름마크=[]
CGV경기소진아맥포스터=[]

CGV인천소진필름마크=[]
CGV인천소진아맥포스터=[]

CGV충남소진필름마크=[]
CGV충남소진아맥포스터=[]

CGV대구소진필름마크=[]
CGV대구소진아맥포스터=[]

CGV전남소진필름마크=[]
CGV전남소진아맥포스터=[]

CGV강원소진필름마크=[]
CGV강원소진아맥포스터=[]

CGV부산소진필름마크=[]
CGV부산소진아맥포스터=[]

CGV=[]
MegaBox=[]
LotteCinema=[]


with open('cgv.txt','r',encoding='UTF-8') as fd:
    reader=csv.reader(fd)
    for row in reader:
        CGV.append(row)
CGV서울.extend(CGV[0])
CGV경기.extend(CGV[1])
CGV인천.extend(CGV[2])
CGV충남.extend(CGV[3])
CGV대구.extend(CGV[4])
CGV전남.extend(CGV[5])
CGV강원.extend(CGV[6])
CGV부산.extend(CGV[7])



#cgv 지점 등록

while True:
    try:
        driver.find_element_by_xpath("//*[contains(text(),'이전 댓글')]").click()
        time.sleep(2)
    except:
        break
                
#모든 더보기 버튼 누르기


time.sleep(2)
#롯시 대전센트럴 킹스맨 아트카드 소진입니다 <-첫 오브젝트


contents = driver.find_elements_by_css_selector('div.cmt_body')

for cont in contents:
    소진지점.append(cont.text)

for content in 소진지점:
    f.write(content+"\n")
f.close()

def check_string():
    with open('소진지점.txt', 'rt', encoding='UTF8') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        
        if '소진' in line:
            print(line)
            소진지점2.append(line)
        elif '끝' in line:
                print(line)
                소진지점2.append(line)

check_string()


print(소진지점2)
f = open('소진지점.txt', 'r+', encoding='UTF8')
f.truncate(0) # 파일비우기
data=f.readlines()
for a in data:
    print(a) #비워졌는지 체크

for element in 소진지점2:
    f.write(element) #텍스트파일에 적기

for line in data:
    print(line) #채워졌는지 체크

f.close()
print("end")


driver.close()

def 서울소진( ): #in () -> user can put 필름마크 or 아맥 포스터
  
    # global 소진지점2
    # global CGV서울소진아맥포스터
    # global CGV서울소진필름마크    
    for s1 in CGV서울:
        for s2 in 소진지점2:
            if s1 in s2:
                if '필름마크' in s2:
                    CGV서울소진필름마크.append(s1)
                
                elif '아맥포스터' in s2:
                    CGV서울소진아맥포스터.append(s1)
    print('서울 필름마크 소진지점: ',CGV서울소진필름마크)
    print('서울 아이맥스 포스터 소진지점: ',CGV서울소진아맥포스터)

        

서울소진()


for s1 in CGV경기:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV경기소진필름마크.append(s1)
              
            elif '아맥포스터' in s2:
                CGV경기소진아맥포스터.append(s1)

print('경기 필름마크 소진지점: ',CGV경기소진필름마크)
print('경기 아이맥스 포스터 소진지점: ',CGV경기소진아맥포스터)


for s1 in CGV인천:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV인천소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV인천소진아맥포스터.append(s1)
               

print('인천 필름마크 소진지점: ',CGV인천소진필름마크)
print('인천 아이맥스 포스터 소진지점: ',CGV인천소진아맥포스터)

for s1 in CGV충남:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV충남소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV충남소진아맥포스터.append(s1) 


print('충남 필름마크 소진지점: ',CGV충남소진필름마크)
print('충남 아이맥스 포스터 소진지점: ',CGV충남소진아맥포스터)


for s1 in CGV대구:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV대구소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV대구소진아맥포스터.append(s1)
                


print('대구 필름마크 소진지점: ',CGV대구소진필름마크)
print('대구 아이맥스 포스터 소진지점: ',CGV대구소진아맥포스터)

for s1 in CGV전남:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV전남소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV전남소진아맥포스터.append(s1)
                


print('전남 필름마크 소진지점: ',CGV전남소진필름마크)
print('전남 아이맥스 포스터 소진지점: ',CGV전남소진아맥포스터)

for s1 in CGV강원:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV강원소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV강원소진아맥포스터.append(s1)
               

print('강원 필름마크 소진지점: ',CGV강원소진필름마크)
print('강원 아이맥스 포스터 소진지점: ',CGV강원소진아맥포스터)

for s1 in CGV부산:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV부산소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV부산소진아맥포스터.append(s1)


print('부산 필름마크 소진지점: ',CGV부산소진필름마크)
print('부산 아이맥스 포스터 소진지점: ',CGV부산소진아맥포스터)
