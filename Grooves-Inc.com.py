import json
from bs4 import BeautifulSoup
import requests
def func(url: str):
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    upc_elements = None
    sku_elements = None
    brand_elements = None
    brand_elements = soup.select_one('div[itemprop="brand"] > meta[itemprop="name"]')
    brand  = brand_elements.get('content')
    sku_elements = soup.select_one('meta[itemprop="sku"]') 
    sku = sku_elements.get('content')
    upc_elements = soup.select_one('meta[itemprop="gtin14"]')
    upc = upc_elements.get('content')
           
    return f"brand :{brand}""\n" f"sku :{sku}""\n" f"upc :{upc}"
print(func("https://www.grooves-inc.com/philips-philips-azur-8000-series-dst8050-steam-iron-philips-hardware-electronic-pZZa1-2101024123.html?utm_source=shop&utm_campaign=homepage&utm_medium=products_by_artist"))