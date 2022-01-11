from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from urllib3.packages.six import StringIO
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 
import csv
import telegram
import re
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
# CGV서울=['강변','대학로','등촌','불광','상봉','성신여대입구','수유','신촌','압구정','여의도','연남','영등포','왕십리','용산','중계','천호']
# CGV경기=['광교','구리','김포','동탄','배곧','소풍','수원','안산','의정부','의정부태흥','이천','일산','죽전','파주야당','판교','평촌','평택']
# CGV인천=['인천','계양','부평','인천','인천연수','청라']
# CGV충남=['대전','대전탄방','대전터미널','세종','천안터미널','천안펜타포트','청주서문']
# CGV대구=['대구스타디움','대구아카데미','대구한일','대구현대']
# CGV전남=['광주금남로','광주첨단','광주터미널','목포평화광장','순천신대','여수웅천','전주고사','전주효자']
# CGV강원=['원주','춘천']
# CGV부산=['경산','김해','동래','북포항','서면','서면삼정타워','센텀시티','양산물금','울산삼산','창원더시티','하단아트몰링']

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
MB오리지널티켓서울=[]
LotteCinema=[]
LC아트카드서울=[]

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
with open('megabox.txt','r',encoding='UTF-8') as fd:
    reader=csv.reader(fd)
    for row in reader:
        MegaBox.append(row)
MB오리지널티켓서울.extend(MegaBox[0])
#megabox



with open('Lotte_cinema.txt','r',encoding='UTF-8') as fd:
    reader=csv.reader(fd)
    for row in reader:
        LotteCinema.append(row)

LC아트카드서울.extend(LotteCinema[0])

print(LC아트카드서울)

print(LC아트카드서울[0])


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


def check_string():
    
    for line in 소진지점:
        
        if '소진' in line:
            print(line)
            소진지점2.append(line)
        elif '끝' in line:
                print(line)
                소진지점2.append(line)

check_string()





driver.close()


def 서울소진( ): #in () -> user can put 필름마크 or 아맥 포스터
  

    for s1 in CGV서울:
        for s2 in 소진지점2:
            if s1 in s2:
                if '필름마크' in s2:
                    CGV서울소진필름마크.append(s1)
                
                elif '아맥포스터' in s2:
                    CGV서울소진아맥포스터.append(s1)
    

        

서울소진()


for s1 in CGV경기:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV경기소진필름마크.append(s1)
              
            elif '아맥포스터' in s2:
                CGV경기소진아맥포스터.append(s1)




for s1 in CGV인천:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV인천소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV인천소진아맥포스터.append(s1)
               



for s1 in CGV충남:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV충남소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV충남소진아맥포스터.append(s1) 





for s1 in CGV대구:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV대구소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV대구소진아맥포스터.append(s1)
                



for s1 in CGV전남:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV전남소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV전남소진아맥포스터.append(s1)
                




for s1 in CGV강원:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV강원소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV강원소진아맥포스터.append(s1)
               



for s1 in CGV부산:
    for s2 in 소진지점2:
        if s1 in s2:
            if '필름마크' in s2:
                CGV부산소진필름마크.append(s1)
                
            elif '아맥포스터' in s2:
                CGV부산소진아맥포스터.append(s1)

new_list=[]
def 정렬(listname):
    global result1
    global listn
    result1=set(listname)

    fixedlist=list(result1)
    listname.clear()
    for v in fixedlist:
        listname.append(v)
    #중복자료제거
    listname.sort()
   
정렬(CGV서울소진필름마크)
정렬(CGV서울소진아맥포스터)
정렬(CGV부산소진필름마크)
정렬(CGV부산소진아맥포스터)
정렬(CGV대구소진필름마크)
정렬(CGV대구소진아맥포스터)
정렬(CGV경기소진필름마크)
정렬(CGV경기소진아맥포스터)
정렬(CGV강원소진필름마크)
정렬(CGV강원소진아맥포스터)
정렬(CGV충남소진아맥포스터)
정렬(CGV충남소진필름마크)
정렬(CGV전남소진아맥포스터)
정렬(CGV전남소진필름마크)
정렬(CGV인천소진아맥포스터)
정렬(CGV서울소진필름마크)



class 굿즈소진:
    class 지역필름마크소진:
        def __init__(self):
            self.서울='서울 필름마크 소진지점: ',CGV서울소진필름마크
            self.부산='부산 필름마크 소진지점: ',str(CGV부산소진필름마크)
            self.경기='경기 필름마크 소진지점: ',CGV경기소진필름마크
            self.인천='인천 필름마크 소진지점: ',CGV인천소진필름마크
            self.강원='강원 필름마크 소진지점: ',CGV강원소진필름마크
            self.전남='전남 필름마크 소진지점: ',CGV전남소진필름마크
            self.충남='충남 필름마크 소진지점: ',CGV충남소진필름마크
            self.대구='대구 필름마크 소진지점: ',CGV대구소진필름마크
    class 지역아이맥스포스터소진:
        def __init__(self):
            self.서울='서울 아이맥스 소진지점: ',CGV서울소진아맥포스터
            self.부산='부산 아이맥스 소진지점: ',CGV부산소진아맥포스터
            self.경기='경기 아이맥스 소진지점: ',CGV경기소진아맥포스터
            self.인천='인천 아이맥스 소진지점: ',CGV인천소진아맥포스터
            self.강원='강원 아이맥스 소진지점: ',CGV강원소진아맥포스터
            self.전남='전남 아이맥스 소진지점: ',CGV전남소진아맥포스터
            self.충남='충남 아이맥스 소진지점: ',CGV충남소진아맥포스터
            self.대구='대구 아이맥스 소진지점: ',CGV대구소진아맥포스터
지역필름마크=굿즈소진().지역필름마크소진()
지역아맥포스터=굿즈소진().지역아이맥스포스터소진()
print(getattr(지역필름마크,'서울')) #replace 지역필름마크 as button choose 필름마크 그리고 '서울'은 입력값 혹은 지역선택으로 바꾸기
print(getattr(지역아맥포스터,'서울')) #""
