import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def print_full_form_handler():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    
    idx = r.text.find('if(this.id=="formBusins")')
    if idx != -1:
        print(r.text[idx:idx+800])

if __name__ == "__main__":
    print_full_form_handler()
