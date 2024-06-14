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
    brand_elements = soup.select_one("div#description-details-content .brand")
    brand  = brand_elements.text.split("Brand: ")[-1].strip()
    mpn_elements = soup.select_one("#details-content meta[itemprop='mpn']") 
    mpn = mpn_elements.get('content')
    upc_elements = soup.select_one("#details-content > meta[itemprop='upc']")
    upc = upc_elements.get('content')
           
    return f"mpn :{mpn}" "\n"f"brand :{brand}""\n" f"upc :{upc}"
print(func("https://www.mdgsales.com/willy-chavarria-charcoal-longsleeve-ruff-neck-t-size-large-esm030x42x092123"))