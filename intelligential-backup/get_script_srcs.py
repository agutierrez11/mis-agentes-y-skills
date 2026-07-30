import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_script_srcs():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    scripts = soup.find_all('script')
    for s in scripts:
        src = s.get('src')
        if src:
            print("Script Src:", src)

if __name__ == "__main__":
    get_script_srcs()
