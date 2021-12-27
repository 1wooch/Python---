from selenium import webdriver
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
소진지점=[]


while True:
    try:
        #더보기=driver.find_element_by_css_selector('div.cmt_page cmt_prev')
        #더보기=driver.find_element_by_css_selector('bt_cmt_page bt_cmt_prev')
        #driver.find_element_by_xpath("//button[@onclick=\"prevCmt('2')\"]").click()
        driver.find_element_by_xpath("//button[@onclick=\"prevCmt('2')\"]").click()
        time.sleep(1)
        #더보기.click()
        #time.sleep(1)

    except:
        break

contents = driver.find_elements_by_css_selector('div.cmt_body')
for content in contents:
    #print(content.text)
    #if '소진' in content:
    #    print(content)
    f.write(content.text+"\n")

f.close()


def check_string():
    with open('소진지점.txt', 'rt', encoding='UTF8') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if '소진' in line:
            print(line)
            소진지점.append(line)
        elif '끝' in line:
                print(line)
                소진지점.append(line)



check_string()
print(소진지점)
f = open('소진지점.txt', 'r+', encoding='UTF8')
f.truncate(0) # 파일비우기
data=f.readlines()
for a in data:
    print(a) #비워졌는지 체크

for element in 소진지점:
    f.write(element) #텍스트파일에 적기

for line in data:
    print(line) #채워졌는지 체크

f.close()
print("end")


driver.close()
