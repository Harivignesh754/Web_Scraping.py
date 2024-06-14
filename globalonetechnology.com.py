import json
from bs4 import BeautifulSoup
import requests

def func(url: str):
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    script_tags = soup.find_all('script', type='application/ld+json')

    sku = None
    brand = None
    upc = None

    for script in script_tags:
        res = json.loads(script.string)
        if isinstance(res, dict):
            if res.get('@type') == 'Product':
                sku = res.get('sku')
                brand_data = res.get('brand')
                if brand_data:
                    brand = brand_data.get('name')
                break
                
    return f"Sku: {sku}\nBrand: {brand}\nupc: {upc}"

print(func("https://www.globalonetechnology.com/872479-b21.htm"))
