import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def print_carga_datos():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp"
    r = requests.get(url, verify=False, timeout=15)
    
    idx = r.text.find('function cargaDatos')
    if idx != -1:
        print(r.text[idx:idx+1000])

if __name__ == "__main__":
    print_carga_datos()
