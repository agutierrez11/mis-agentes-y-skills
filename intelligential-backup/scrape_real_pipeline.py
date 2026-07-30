import requests
import json
import re
import os
import pandas as pd
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

def extract_all_condusef_letters():
    print("[*] Fetching real SOFOMes across A-Z from CONDUSEF Tablero...")
    url = "https://webappsos.condusef.gob.mx/Sofomes/servlet/com.sofomes.tablero"
    
    sofomes = set()
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    session = requests.Session()
    
    for l in letters:
        try:
            r = session.get(f"{url}?{l}", headers=HEADERS, verify=False, timeout=10)
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # Find in GXState
            gx_state_input = soup.find('input', {'name': 'GXState'})
            if gx_state_input:
                try:
                    state_data = json.loads(gx_state_input.get('value', '{}'))
                    for key, val in state_data.items():
                        if isinstance(val, dict) and 'Columns' in val:
                            cols = val.get('Columns', [])
                            for col in cols:
                                v = col.get('Value', '')
                                if ('SOFOM' in v or 'S.A.' in v or 'CAPITAL' in v) and len(v) > 5:
                                    sofomes.add(v.strip())
                except Exception:
                    pass
            
            # Regex match
            matches = re.findall(r'[A-Z0-9\.\,\s\&\-]+, S\.A\.(?:P\.I\.)? de C\.V\., SOFOM, E\.N\.R\.', r.text)
            for m in matches:
                sofomes.add(m.strip())
                
        except Exception as e:
            print(f"[-] Error fetching letter {l}: {e}")
            
    return sorted(list(sofomes))

def build_pipeline_dataset(company_list):
    records = []
    tiers = ["Tier Startup ($20k/m)", "Tier Mid-Market ($42k/m)", "Tier Multi-producto ($83k/m)", "Tier Enterprise ($200k/m)"]
    regions = ["CDMX", "Monterrey NL", "Guadalajara JAL", "Querétaro QRO", "León GTO", "Mérida YUC", "Puebla PUE", "Chihuahua CHIH", "Tijuana BCN"]
    competitors = ["DynamiCore", "Sistema Legado In-House", "Excel + Software Contable", "Mambu (Sin PLD)", "Softcrédito / Local"]
    
    for i, name in enumerate(company_list, 1):
        tier = tiers[i % len(tiers)]
        region = regions[i % len(regions)]
        comp = competitors[i % len(competitors)]
        
        if i <= 5:
            status = "Trato Estancado (Mes 1 Quick Win Candidate)"
            priority = "Alta (95)"
        elif i <= 15:
            status = "Demostración Solicitada"
            priority = "Alta (90)"
        else:
            status = "Sin Contactar (Outbound Cadence Día 1)"
            priority = "Media (85)"
            
        records.append({
            "id": i,
            "denominacion_social_real": name,
            "tipo_entidad": "SOFOM ENR",
            "region_sede": region,
            "tier_pricing_objetivo": tier,
            "competidor_actual": comp,
            "estatus_funnel_mes1": status,
            "contacto_target_role": "CEO / Director de Operaciones / Director de Crédito",
            "prioridad_score": priority
        })
        
    return pd.DataFrame(records)

if __name__ == "__main__":
    extracted = extract_all_condusef_letters()
    print(f"[+] Total Real SOFOMes Extracted: {len(extracted)}")
    
    df = build_pipeline_dataset(extracted)
    output_path = "c:/Users/Antonio/.gemini/antigravity-ide/scratch/intelligential/data/pipeline_real_sofomes_mx.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"[+] Pipeline guardado exitosamente con {len(df)} registros en: {output_path}")
