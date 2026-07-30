import requests
from bs4 import BeautifulSoup
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def find_ajax_urls():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    
    matches = re.findall(r'(\/[a-zA-Z0-9_\/]+\.jsp|\.\.\/[a-zA-Z0-9_\/]+\.jsp|[a-zA-Z0-9_]+\.jsp)', r.text)
    print("Unique JSPs referenced:", set(matches))

if __name__ == "__main__":
    find_ajax_urls()
