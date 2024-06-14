import json
from bs4 import BeautifulSoup
import requests
def func(url: str):
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    mpn_elements = None
    brand_elements = None
    brand_elements = soup.select_one('meta[itemprop="brand"]')
    brand  = brand_elements.get('content')
    mpn_elements = soup.select_one('meta[itemprop="mpn"]') 
    mpn = mpn_elements.get('content')
    return f"mpn :{mpn}" "\n"f"brand :{brand}"
print(func("https://www.inksmile.com/compatible-hp-507x-507a-toner-cartridge--4-pack.html"))