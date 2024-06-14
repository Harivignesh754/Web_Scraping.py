import json
from bs4 import BeautifulSoup
import requests
import re

def func(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    script = soup.find_all('script', type='application/ld+json')
    mpn = None
    title = None
    for items in script:
        try:
            json_text = items.string
            if json_text:
                # Clean up the JSON text
                json_text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_text)
                res = json.loads(json_text)
                if isinstance(res, dict):
                    if res.get('@type') == 'Product':
                        mpn = res.get('mpn')
                        title = res.get('name')
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    return f"mpn: {mpn}""\n" f"titel: {title}"

print(func("https://archmemory.com/dell-memory-snpvny72c-16g-ab949334-16gb-1rx8-ddr5-sodimm-4800mhz-ram/"))


