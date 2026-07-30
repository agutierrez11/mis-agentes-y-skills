import requests
from bs4 import BeautifulSoup
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_sipres_search_post():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/resulbusq.jsp"
    
    # Payload searching for sector 69 (SOFOM ENR)
    payload = {
        'psec': '69',
        'pedo': '0', # All states
        'psta': '1', # Activa / Operando
        'nom': ''
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    r = requests.post(url, data=payload, headers=headers, verify=False, timeout=20)
    print(f"SIPRES Search Status: {r.status_code}, Length: {len(r.text)}")
    
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.find_all('table')
    print(f"Found {len(tables)} tables in search results.")
    
    for i, t in enumerate(tables):
        rows = t.find_all('tr')
        if len(rows) > 0:
            print(f"Table {i} ({len(rows)} rows):")
            for row in rows[:5]:
                cols = [c.text.strip().replace('\n', ' ') for c in row.find_all(['td', 'th'])]
                print("  Cols:", cols)

if __name__ == "__main__":
    test_sipres_search_post()
