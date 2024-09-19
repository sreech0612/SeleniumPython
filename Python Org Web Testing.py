from logging import exception

import selenium
from selenium import  webdriver
from  selenium.webdriver.chrome.service import Service as ChromeService
import webdriver_manager
from  webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver.get('https://www.python.org/')
cur_title = driver.title
expected_title = 'Welcome to Python.org'
if cur_title != expected_title:
    raise exception('Went to Python.org but got wrong title. Current_title: {}'.format(cur_title))
pypi_header_link = '#top > nav > ul > li.pypi-meta > a'
pypi_header_link_element = driver.find_element(By.CSS_SELECTOR,pypi_header_link)
pypi_header_link_element.click()
time.sleep(5)
driver.get('https://pypi.org/')
cur_url = driver.current_url
expected_url = 'https://pypi.org/'
if cur_url == expected_url:
    print("Pass")
else:
    print("Clicked on pypi link but the url is: {}".format(cur_url))

