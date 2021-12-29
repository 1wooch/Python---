from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 
#from find_text import check_string
from selenium.common.exceptions import NoSuchElementException

f=open("소진지점.txt",'w',encoding='UTF-8')

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://extmovie.com/movietalk/71696227')
driver.implicitly_wait(5)
소진지점=[]


buttons = driver.find_elements_by_xpath("//*[contains(text(),'이전 댓글')]")
for btn in buttons:
    btn.click()




