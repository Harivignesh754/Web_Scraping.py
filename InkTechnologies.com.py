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
                mpn = res.get('mpn')
                brand = res.get('brand')
                break
                
    return f"mpn: {mpn}\nBrand: {brand}\nupc: {upc}"

print(func("https://www.inktechnologies.com/epson-502-inkjet-ultra-high-capacity-bundle-pack-9-bottles-compatible"))
