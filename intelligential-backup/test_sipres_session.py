import requests
from bs4 import BeautifulSoup
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_with_session():
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp'
    })
    
    # 1. GET index.jsp
    r1 = session.get('https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp', verify=False, timeout=15)
    print("GET index.jsp cookies:", session.cookies.get_dict())
    
    # 2. POST resulbusq.jsp
    payload = {
        'tipo': '1',
        'pnom': '',
        'pedo': '0',
        'psec': '69',
        'psta': '1'
    }
    
    r2 = session.post('https://webapps.condusef.gob.mx/SIPRES/jsp/pub/resulbusq.jsp', data=payload, verify=False, timeout=30)
    print(f"POST resulbusq.jsp status: {r2.status_code}, length: {len(r2.text)}")
    print("HTML snippet:", r2.text[:800])

if __name__ == "__main__":
    fetch_with_session()
