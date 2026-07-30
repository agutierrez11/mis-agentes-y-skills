import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_form_submit_code():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    
    for m in re.finditer(r'formBusins', r.text):
        idx = m.start()
        print("Snippet:", r.text[max(0, idx-200):min(len(r.text), idx+300)])
        print("="*50)

if __name__ == "__main__":
    get_form_submit_code()
