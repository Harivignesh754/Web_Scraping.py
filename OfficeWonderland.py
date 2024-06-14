from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import os

chrome_path = os.getenv('chrome')
service = Service(chrome_path + "/chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = chrome_path + "/chrome.exe"
web_driver = webdriver.Chrome(service=service, options=options)
web_driver.maximize_window()

def get_data(url: str):
    web_driver.get(url)
    
    gtin = None
    sku  = None
    brand = None
    try:
        sku_element = web_driver.find_element(By.CSS_SELECTOR, "div.elementor-element.elementor-element-1f79434.elementor-widget.elementor-widget-text-editor > div.elementor-widget-container")
        sku = sku_element.text.split("SKU:")[-1].strip()
        brand_element = web_driver.find_element(By.CSS_SELECTOR, "div.product_title.entry-title.elementor-heading-title.elementor-size-default")
        brand = brand_element.text.split(" ")[0].strip()
        script = web_driver.find_element(By.CSS_SELECTOR, "script[id='woo-add-gtin-js-extra']")
        script_content = script.get_attribute('innerHTML')
        if 'var wooGtinVars = ' in script_content:
            json_scr = script_content.split("var wooGtinVars = ")[1].strip().strip(';')
            scrap = json.loads(json_scr)
            gtin = scrap.get('gtin')
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return f"gtin: {gtin}\n"f"sku: {sku}\n"f"brand: {brand}\n"

print(get_data("https://officewonderland.com/listings/viewsonic-px748-4k-4000-lumen-hdr-4k-home-theater-dlp-projector/"))
web_driver.quit()





