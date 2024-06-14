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
upc =  None
mpn = None
brand = None
def get_data(url: str):
    web_driver.get(url)
    time.sleep(4)
    upc = web_driver.find_element(By.CSS_SELECTOR, "#divProdInfoWrapper_392 > div.prod-metadata > div:nth-child(3) > span")
    brand = web_driver.find_element(By.CSS_SELECTOR,"#divProdInfoWrapper_392 > h1 > span")
    mpn = web_driver.find_element(By.CSS_SELECTOR,"#divProdInfoWrapper_392 > div.prod-metadata > div.prod-mfgpartno > span")
    brand_final = brand.text.split(" ")[0]
    return f"mpn :{mpn.text}" "\n" f"upc :{upc.text}" "\n" f"brand :{brand_final}"
    
print(get_data("https://www.colamco.com/product/extreme-networks-extremeswitching-x465-x465-48p-ethernet-switch-x465-48p-1938559"))
web_driver.quit()
