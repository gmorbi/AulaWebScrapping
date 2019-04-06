# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:42:23 2019

@author: gemva
"""
# Trabalho Aula 1
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options, executable_path ="C:/Users/gemva/Desktop/POS/WebScrapping/chromedriver")
browser.get('https://www.brewersfriend.com/search/')

time.sleep(5)

soup = BeautifulSoup(browser.page_source, 'html.parser')

data = []
for tr in soup.find_all('table', {'class':'recipeitems'}):
    cols = tr.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    
print(data)
browser.close()