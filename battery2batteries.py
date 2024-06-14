import json
from bs4 import BeautifulSoup
import requests

def get_data(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    script = soup.find_all('script', type='text/javascript')
    scrap = None
    mpn = None
    gtin = None
   
    for item in script:
        if 'var BCData'in item.text:
            json_scr = item.text.split("= ")[1].split("};")[0] + "}"
            scrap = json.loads(json_scr)
            break
    if isinstance(scrap,dict):
            product_attributes =  scrap.get('product_attributes')
            mpn = product_attributes.get('mpn')
            gtin = product_attributes.get('upc')
            
    return f"mpn :{mpn}" "\n"  f"upc :{gtin}"           
       
print(get_data("https://www.battery2batteries.com/duracell-procell-aa-batteries-pc1500-industrial-144-case-constant-power/"))   

