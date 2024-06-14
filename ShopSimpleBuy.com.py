import json

from bs4 import BeautifulSoup
import requests
import sys


brand =None
def get_data(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    brand = soup.select_one("p[itemprop='brand']")
    
    script = soup.find('script', type="application/json", id="ProductJson-product-template")
    scrap = json.loads(script.text)
    if isinstance(scrap, dict):
        variants = scrap.get('variants')
    if variants:
        sku = variants[0].get('sku')
        return f"sku: {sku}\n"f"brand: {brand.text}\n"
    

print(get_data("https://shopsimplebuy.com/products/greentech-pa3781u-1brs-battery-for-toshiba-satellite-e200-e205-10-8v-56whr-pabas216-v000200020"))
