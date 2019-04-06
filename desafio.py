"""
Created on Sat Apr  6 13:56:55 2019

@author: gemva
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

cidades = {'Bauru, São Paulo, Brasil', 'Lençóis Paulista, São Paulo, Brasil', 'Botucatu, São Paulo, Brasil'}
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options, executable_path ="C:/Users/gemva/Desktop/POS/WebScrapping/chromedriver")

browser.get('https://weather.com/pt-BR/clima/10dias/l/b1fe19a3e85170816dd4fe389d9e6477fdb95f5c9b39f836a13f1950106dd183')

time.sleep(5)

for cities in cidades:
    pesquisa = browser.find_element(By.CSS_SELECTOR,".theme__inputElement__4bZUj.input__inputElement__1GjGE") 
    pesquisa.send_keys(cities)
    
    time.sleep(5)
    
    select = browser.find_element(By.CSS_SELECTOR,".styles__item__3sdr8.styles__selected__SEH0e")
    
    time.sleep(5)
    
    select.click()
    
    print('\n ' + cities)
    
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    
    data = []
    for tr in soup.find_all('table', {'class':'twc-table'}):
        cols = tr.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
        
    print(data)

browser.close()