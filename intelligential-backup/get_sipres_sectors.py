import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_sipres_sectors():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    psec = soup.find('select', {'id': 'psec'}) or soup.find('select', {'name': 'psec'})
    sectors = {}
    if psec:
        for opt in psec.find_all('option'):
            val = opt.get('value')
            txt = opt.text.strip()
            if val:
                sectors[val] = txt
    print("Sectors found:", json.dumps(sectors, indent=2, ensure_ascii=False))
    return sectors

if __name__ == "__main__":
    get_sipres_sectors()
