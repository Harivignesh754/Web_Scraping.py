import json
from bs4 import BeautifulSoup
import requests
import sys


brand =None
def get_data(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
   
    
    script = soup.find_all('script', type='application/ld+json')

    gtin = None
    sku = None
    brand = None

    for items in script:
        res = json.loads(items.string)
        if isinstance(res,dict):
            if res.get('@type') == 'Product':
                sku = res.get('sku')
                gtin = res.get('gtin12')
                brand = res.get('brand').get('name')
    return f"gtin: {gtin}\n"f"sku: {sku}\n"f"brand: {brand}"

print(get_data("https://falcontech.com/collections/bulk-ethernet-cat5e-indoor-pvc-cable/products/182str-spl-b-trane-pp-18-2-trane-temperature-control-cable-2-conductor-18-awg-shielded-plenum-purple-1000-feet"))
