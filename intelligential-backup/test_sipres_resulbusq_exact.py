import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_sipres_active_sofomes():
    url = "https://webapps.condusef.gob.mx/SIPRES/jsp/pub/resulbusq.jsp"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://webapps.condusef.gob.mx/SIPRES/jsp/pub/index.jsp'
    }
    
    payload = {
        'tipo': '1',
        'pnom': '',
        'pedo': '', # All States
        'psec': '69', # Sector 69 = SOFOM ENR
        'psta': '1'  # Status 1 = OPERANDO / ACTIVA
    }
    
    print("[*] Enviando consulta POST a SIPRES (resulbusq.jsp) para SOFOM ENR ACTIVAS (psec=69, psta=1)...")
    r = requests.post(url, data=payload, headers=headers, verify=False, timeout=60)
    
    print(f"[+] Respuesta recibida. HTTP {r.status_code}, Tamaño: {len(r.text)} bytes.")
    
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.find_all('table')
    
    records = []
    
    for t in tables:
        rows = t.find_all('tr')
        print(f"Table rows count: {len(rows)}")
        for r_idx, row in enumerate(rows):
            cols = [c.text.strip().replace('\n', ' ') for c in row.find_all(['td', 'th'])]
            if len(cols) >= 3:
                # Typically: [No, Denominacion Social, Estado, Estatus, Sector, Detail Link]
                records.append(cols)
                
    print(f"[+] Total filas extraídas: {len(records)}")
    if records:
        print("Sample header/first row:", records[:3])
        
    return records

if __name__ == "__main__":
    fetch_sipres_active_sofomes()
