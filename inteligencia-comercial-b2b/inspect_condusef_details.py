import requests
import json
import re
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def inspect_condusef_detailed_fields():
    url = "https://webappsos.condusef.gob.mx/Sofomes/servlet/com.sofomes.tablero"
    session = requests.Session()
    
    r = session.get(url, verify=False, timeout=15)
    gx_match = re.search(r'name="GXState" value="([^"]+)"', r.text)
    soup_state = gx_match.group(1) if gx_match else ""
    
    payload = {
        'vNUMPAG': '15',
        'GRID1_nFirstRecordOnPage': '0',
        'GXState': soup_state,
        '_EventName': '',
        '_EventGridId': '',
        '_EventRowId': ''
    }
    
    r2 = session.post(url, data=payload, headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=False, timeout=20)
    
    print("[*] Inspecting HTML tables and GXState fields...")
    
    # Check JSON GXState in r2
    gx2_match = re.search(r'name="GXState" value="([^"]+)"', r2.text)
    if gx2_match:
        raw_json = gx2_match.group(1).replace('&quot;', '"')
        parsed = json.loads(raw_json)
        print("Keys in GXState:", list(parsed.keys()))
        if 'Columns' in str(parsed):
            print("Sample grid data structure:", json.dumps(parsed, indent=2)[:1500])
            
    # Also inspect HTML table header and row contents
    soup = BeautifulSoup(r2.text, 'html.parser')
    tables = soup.find_all('table')
    for i, t in enumerate(tables):
        rows = t.find_all('tr')
        if len(rows) > 1:
            print(f"Table {i} has {len(rows)} rows. First 3 rows:")
            for r_idx, row in enumerate(rows[:3]):
                cols = [c.text.strip() for c in row.find_all(['td', 'th'])]
                print(f"  Row {r_idx}: {cols}")

if __name__ == "__main__":
    inspect_condusef_detailed_fields()
