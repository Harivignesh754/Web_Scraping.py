import json
from bs4 import BeautifulSoup
import requests

def func(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    script = soup.find_all('script', type='application/ld+json')

    gtin = None
    brand = None
    mpn = soup.select_one("div#mpn")
    for item in script:
        
        res = json.loads(item.string)
        if isinstance(res, list):
            for obj in res:
                if isinstance(obj, dict) and obj.get('@type') == 'Product':
                    gtin = obj.get('gtin13')
                    brand_data = obj.get('brand')
    return f"mpn: {mpn.text.strip()}\nupc: {gtin}\nbrand: {brand_data}"
print(func("https://www.totallyfurniture.com/harmony-outdoor-patio-aluminum-coffee-table-eei-2605-whi"))
