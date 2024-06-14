import json
from bs4 import BeautifulSoup
import requests
def func(url: str):
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    script = soup.find_all('script', type='application/ld+json')

    gtin = None
    mpn = None
    brand = None

    for items in script:
        res = json.loads(items.string)
        if isinstance(res,dict):
            if res.get('@type') == 'Product':
                mpn = res.get('mpn')
                gtin = res.get('gtin13')
                brand = res.get('brand').get('name')
    return f"mpn :{mpn}" "\n" f"upc :{gtin}" "\n" f"brand :{brand}"
print(func("https://www.lightingselection.com/kichler-midi-1-light-12-inch-picture-light-in-black-with-ribbed-metal-cylinder-shade-52649bk.html"))