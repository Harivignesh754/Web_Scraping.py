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
    # upc_elements = web_driver.find_element(By.CSS_SELECTOR,"#specs > div:nth-child(6) > span")
    brand = web_driver.find_element(By.CSS_SELECTOR,"#specs > div:nth-child(1) > span > a")
    mpn = web_driver.find_element(By.CSS_SELECTOR,"#specs > div:nth-child(4) > span")
    upc = web_driver.find_element(By.CSS_SELECTOR, "#specs > div:nth-child(6) > span")
    return f"mpn :{mpn.text}" "\n" f"upc :{upc.text}" "\n" f"brand :{brand.text}"
    

print(get_data("https://www.superwarehouse.com/canon-pfi-1300-photo-magenta-pigment-ink-tank-330ml-0816c001aa.html"))
web_driver.quit()



