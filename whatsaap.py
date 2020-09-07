# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:19:06 2020

@author: Sagar panda
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver= webdriver.Chrome("C:\Chromedriver\chromedriver")
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)
target='"Sree"' # NAME OF CONTACT
string = " HEY HELLO THERE "# MESSEGE U WANT TO SEND
x_arg='//span[contains(@title, ' + target + ')]'
target=WebDriverWait(driver,150).until(EC.presence_of_element_located((By.XPATH,x_arg)))
target.click()
input_box=driver.find_element_by_class_name('_1Plpp')
for i in range(200):#TIMES U WANT TO SEND 
    input_box.send_keys(string+Keys.ENTER)
