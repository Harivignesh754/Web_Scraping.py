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

mpn = None
brand = None
def get_data(url: str):
    web_driver.get(url)
    time.sleep(4)
    brand = web_driver.find_element(By.CSS_SELECTOR,"div.d-inline.mfr-partNum > a")
    mpn = web_driver.find_element(By.CSS_SELECTOR,"div.categories.mfr-details div.d-inline.mfr-partNum")
    return f"mpn :{mpn.text}" "\n"f"brand :{brand.text}"
    
print(get_data("https://itdevicesonline.com/product-details/207656"))
web_driver.quit()
