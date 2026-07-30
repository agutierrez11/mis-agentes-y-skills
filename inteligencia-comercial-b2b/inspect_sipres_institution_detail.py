import requests
import json
import re
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_all_sipres_names():
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    all_raw_names = set()
    
    for char in alphabet:
        url = f"https://webapps.condusef.gob.mx/SIPRES/jsp/pub/nombresins.jsp?query={char}"
        try:
            r = session.get(url, verify=False, timeout=15)
            if r.status_code == 200:
                items = r.json()
                print(f"Query '{char}': returned {len(items)} items.")
                for item in items:
                    all_raw_names.add(item)
        except Exception as e:
            print(f"Error querying {char}: {e}")
            
    print(f"\n[+] Total unique institution strings captured from SIPRES: {len(all_raw_names)}")
    
    # Analyze items
    sofom_items = []
    short_names = []
    
    for name in sorted(list(all_raw_names)):
        if "(nombre corto)" in name:
            short_names.append(name)
        elif any(k in name.upper() for k in ['SOFOM', 'ARRENDADORA', 'FINANCIERA', 'FACTORAJE', 'LEASING', 'CREDITO']):
            sofom_items.append(name)
            
    print(f"[+] Total SOFOMes / Arrendadoras full corporate names: {len(sofom_items)}")
    print(f"[+] Total short names: {len(short_names)}")
    
    # Print sample of short names vs full names
    print("\nSample full names:")
    for fn in sofom_items[:5]:
        print("  -", fn)
        
    print("\nSample short names:")
    for sn in short_names[:5]:
        print("  -", sn)

if __name__ == "__main__":
    fetch_all_sipres_names()
