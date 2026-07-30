import requests
import re
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def inspect_sipres():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    print(f"Status: {r.status_code}, Length: {len(r.text)}")
    
    soup = BeautifulSoup(r.text, 'html.parser')
    forms = soup.find_all('form')
    print(f"Found {len(forms)} forms.")
    for f in forms:
        print("Form Action:", f.get('action'))
        print("Form Method:", f.get('method'))
        for inp in f.find_all(['input', 'select']):
            print("  Input/Select:", inp.get('name'), inp.get('type'), [o.get('value') for o in inp.find_all('option')[:5]])

if __name__ == "__main__":
    inspect_sipres()
