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


buttons = driver.find_elements_by_xpath("//*[contains(text(),'이전 댓글 ')]")
#[<selenium.webdriver.remote.webelement.WebElement (session="dc2ddcb8396e852eb3122e04b04b5436", element="4a89bf7e-78ea-4712-ae5d-7bf8c04e4fab")>]
#for btn in buttons:
#    btn.click()

for element in buttons:
    print(element)
    print("1")
    element.click()
    print("2")
#driver.implicitly_wait(10)
# buttons1 = driver.find_elements_by_xpath("//*[contains(text(),'이전 댓글 ')]")
# print("3")
# for element1 in buttons1:
#     print("4")
#     print(element1)
#     element1.click()
#     print("5")


