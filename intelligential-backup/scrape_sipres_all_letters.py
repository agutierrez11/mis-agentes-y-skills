import requests
import json
import re
import os
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

def extract_condusef_all_pages():
    print("[*] Extraendo catálogo completo de SOFOMes desde CONDUSEF Tablero...")
    url = "https://webappsos.condusef.gob.mx/Sofomes/servlet/com.sofomes.tablero"
    
    session = requests.Session()
    r = session.get(url, headers=HEADERS, verify=False, timeout=20)
    
    all_sofomes = set()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for char in alphabet:
        print(f"[*] Consultando letra/carácter '{char}' en CONDUSEF...")
        try:
            target_url = f"{url}?{char}"
            res = session.get(target_url, headers=HEADERS, verify=False, timeout=15)
            
            matches = re.findall(r'([A-Z0-9\.\,\s\&\-\–\—\(\)]+(?:SOFOM|S\.A\.P\.I|S\.A\.|FINANCIERA|ARRENDADORA|CAPITAL)[A-Z0-9\.\,\s\&\-\–\—\(\)]*)', res.text, re.IGNORECASE)
            
            for m in matches:
                clean_name = m.strip()
                if len(clean_name) > 10 and ("SOFOM" in clean_name.upper() or "S.A." in clean_name.upper() or "S.A.P.I." in clean_name.upper()):
                    clean_name = re.sub(r'<[^>]+>', '', clean_name)
                    clean_name = re.sub(r'\s+', ' ', clean_name).strip()
                    if len(clean_name) > 10:
                        all_sofomes.add(clean_name)
                        
            gx_match = re.search(r'name="GXState" value="([^"]+)"', res.text)
            if gx_match:
                try:
                    state_raw = gx_match.group(1).replace('&quot;', '"')
                    state_json = json.loads(state_raw)
                    for k, v in state_json.items():
                        if isinstance(v, dict) and 'Columns' in v:
                            for col in v.get('Columns', []):
                                val_str = col.get('Value', '')
                                if len(val_str) > 10 and ('SOFOM' in val_str or 'S.A.' in val_str):
                                    all_sofomes.add(val_str.strip())
                except Exception:
                    pass
                    
        except Exception as e:
            print(f"[-] Error al consultar letra '{char}': {e}")
            
    return sorted(list(all_sofomes))

if __name__ == "__main__":
    sofomes = extract_condusef_all_pages()
    print(f"[+] TOTAL DE REGISTROS EXTRAIDOS DE CONDUSEF: {len(sofomes)}")
    
    output_path = "c:/Users/Antonio/.gemini/antigravity-ide/scratch/intelligential/data/full_condusef_directory.csv"
    df = pd.DataFrame({"id": range(1, len(sofomes) + 1), "denominacion_social_oficial": sofomes})
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"[+] Archivo guardado exitosamente en: {output_path}")
