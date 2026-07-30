import requests
from bs4 import BeautifulSoup
import re
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_sipres_js():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    scripts = soup.find_all('script')
    for s in scripts:
        if s.string:
            if 'psec' in s.string or 'busq' in s.string.lower() or 'ajax' in s.string.lower():
                print("--- SCRIPT ---")
                print(s.string[:1000])

if __name__ == "__main__":
    get_sipres_js()
