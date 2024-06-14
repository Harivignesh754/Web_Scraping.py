import json
from bs4 import BeautifulSoup
import requests
def func(url: str):
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    upc_elements = None
    mpn_elements = None
    brand_elements = None
    upc = None
    brand_elements = soup.select_one('meta[name="manufacturer"]')
    brand  = brand_elements.get('content')
    mpn = soup.select_one("div.attr-prod.attr-mfg_part .value") 
    
    upc_elements = soup.select('ul.specification-list > li.child')
    for upc_item in upc_elements:
        if 'UPC' in upc_item.text:
            upc = upc_item.text.split("UPC")[-1].strip()        
            break
        else:
            upc_elements = soup.select('div.attr-prod.attr-upc')
            for upc_item in upc_elements:
                if 'UPC:' in upc_item.text:
                    upc = upc_item.text.split("UPC:")[-1].strip()        
                    break        
        
    return f"mpn :{mpn.text}" "\n"f"brand :{brand}""\n" f"upc :{upc}"
print(func("https://bluesquarepower.com/9sx2000g.html"))