from bs4 import BeautifulSoup
import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_path = os.getenv('chrome')
service = Service(chrome_path + "/chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = chrome_path + "/chrome.exe"
web_driver = webdriver.Chrome(service = service,options = options)
web_driver.maximize_window()

def get_data(url: str):
    web_driver.get(url)
    time.sleep(3)
    spec = web_driver.find_elements(By.CSS_SELECTOR, "h3[class='sc-fe064f5c-0 cJJgsH h-margin-b-none']")
    for spec_lst in spec:
        if 'Specifications' in spec_lst.text:
            time.sleep(3)
            spec_lst.click()
    upc_elements = web_driver.find_elements(By.CSS_SELECTOR, "div[data-test='item-details-specifications'] > div")
    time.sleep(3)
    upc_final = None
    for upc in upc_elements:
        if 'UPC:' in upc.text:
            upc_final = upc.text.split(':')[1].strip()
            break
    title_element = web_driver.find_element(By.CSS_SELECTOR, "#pdp-product-title-id")
    title_text = title_element.text
   
    return f"upc :{upc_final}" "\n" f"brand :{title_text}"
    

print(get_data("https://www.target.com/p/coca-cola-12pk-12-fl-oz-cans/-/A-12953464#lnk=sametab"))
web_driver.quit()

