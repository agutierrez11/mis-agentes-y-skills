import requests
from bs4 import BeautifulSoup
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def find_formbusins_js():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    
    matches = re.findall(r'formBusins[^\n\}]+', r.text)
    print("Matches for formBusins:", matches)
    
    btn_matches = re.findall(r'entra[^\n\}]+', r.text)
    print("Matches for entra:", btn_matches[:10])

if __name__ == "__main__":
    find_formbusins_js()
