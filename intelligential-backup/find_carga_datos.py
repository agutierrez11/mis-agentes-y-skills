import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def find_carga_datos():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    
    for m in re.finditer(r'cargaDatos', r.text):
        idx = m.start()
        print("Snippet:", r.text[max(0, idx-100):min(len(r.text), idx+400)])
        print("="*50)

if __name__ == "__main__":
    find_carga_datos()
