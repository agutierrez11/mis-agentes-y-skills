import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def inspect_sipres_full_html():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    for f in soup.find_all('form'):
        print("--- FORM ---")
        print("Attributes:", f.attrs)
        for input_tag in f.find_all(['input', 'select', 'button']):
            print("  Field:", input_tag.name, input_tag.get('name'), input_tag.get('id'), input_tag.get('value'))

if __name__ == "__main__":
    inspect_sipres_full_html()
