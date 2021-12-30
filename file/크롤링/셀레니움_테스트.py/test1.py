from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 
#from find_text import check_string
f=open("소진지점.txt",'w',encoding='UTF-8')

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://extmovie.com/movietalk/71696227')
driver.implicitly_wait(5)
소진지점=[] #before sorting
소진지점2=[] #after sorting by '소진' ,'끝'
테스트=""

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
