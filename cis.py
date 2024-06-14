from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

chrome_path = os.getenv('chrome')
service = Service(chrome_path + "/chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = chrome_path + "/chrome.exe"
web_driver = webdriver.Chrome(service=service, options=options)
web_driver.maximize_window()

def get_data(url: str):
    web_driver.get(url)
    
    upc_final = None
    brand_final = None
    mpn_lines = None
    
    upc_elements = web_driver.find_elements(By.CSS_SELECTOR, "ul.small-block-grid-1.medium-block-grid-2.large-block-grid-2.columns tr")
    brand_elements = web_driver.find_elements(By.CSS_SELECTOR, "ul.small-block-grid-1.medium-block-grid-2.large-block-grid-2.columns tr")
    mpn_elements = web_driver.find_element(By.CSS_SELECTOR, "#ctl00_PageContent_pnlContent > div.product-detail-page.product-detail-page-v4 > div:nth-child(3) > div.small-12.medium-9.columns > div.row > div.small-12.medium-7.columns.product-overview > span > ul > li:nth-child(1)")
    
    for upc in upc_elements:
        if 'Retail UPC:' in upc.text:
            upc_final = upc.text.split('Retail UPC:')[-1].strip()
            break
    
    for brand in brand_elements:
        if 'Brand:' in brand.text:
            brand_final = brand.text.split('Brand:')[-1].replace("®", "").strip()
            break

    if mpn_elements:
        mpn_lines = mpn_elements.text.split(":")[1].strip()
    return f"mpn :{mpn_lines}" "\n" f"upc :{upc_final}" "\n" f"brand :{brand_final}"
print(get_data("https://www.cleanitsupply.com/p-114883/diversey-oxivir-tb-one-step-disinfectant-cleaner-32-oz-spray-dvo4277285ea.aspx"))
web_driver.quit()
