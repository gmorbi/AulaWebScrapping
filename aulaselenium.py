# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:37:32 2019

@author: gemva
"""
# Cadastra Correntista

from selenium import webdriver
browser = webdriver.Chrome(executable_path ="C:/Users/gemva/Desktop/POS/WebScrapping/chromedriver")
browser.get('http://192.168.6.192:8080/correntista/novo')
nome = browser.find_element_by_name("nome");
email = browser.find_element_by_name("email");
nome.send_keys("Jose da silva");
email.send_keys("josedasilva@email.com");
send = browser.find_element_by_id("button1");
send.click();
browser.close();


#Cadastra Contas
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options, executable_path ="C:/Users/gemva/Desktop/POS/WebScrapping/chromedriver")
browser.get('http://192.168.6.192:8080/conta/novo')
saldo = browser.find_element_by_name("saldo");
saldo.send_keys("100.0");
combo = Select(browser.find_element_by_name("correntista"))
combo.select_by_visible_text("Jose da silva")
tipo_conta = browser.find_element_by_name("tipoConta");
tipo_conta.click();
saldo.submit();
#print(browser.page_source)
browser.close()

