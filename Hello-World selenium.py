# -*- coding: utf-8 -*-
"""
@author: Kaushal Barhate

Printing Hello World on https://write-box.appspot.com/ using selenium and python

Steps for installing selenium:
1) Install selenium webdriver from https://chromedriver.chromium.org/downloads
2) Create a folder in C drive with name webdrivers and copy contents of downloaded folder to C://webdrivers
3) Install selenium in your system by typing the following command - "pip install selenium"
"""

from selenium import webdriver
driver = webdriver.Chrome(r"C:\\webdrivers\\chromedriver.exe")
driver.implicitly_wait(15) 
driver.get('https://write-box.appspot.com/')
driver.find_element_by_xpath('/html/body/div[2]/textarea').send_keys("Hello World")
