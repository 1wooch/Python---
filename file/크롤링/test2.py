from selenium import webdriver
import time
url = 'https://entertain.naver.com/ranking/comment/list?oid=022&aid=0003409199'

#웹 드라이버
driver = webdriver.Chrome('C:\Python 기초\file\크롤링\chromedriver.exe')
driver.implicitly_wait(30)
driver.get(url)