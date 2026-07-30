import requests
import json
import os
import time
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = "fc-a826332a3caa44278ce22953865de09a"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def extract_condusef_full_catalog():
    print("[*] Obteniendo el catálogo completo del Tablero CONDUSEF (Servlet GeneXus)...")
    url = "https://webappsos.condusef.gob.mx/Sofomes/servlet/com.sofomes.tablero"
    
    # Send request requesting full list (vNUMPAG = 1 means 'Todos')
    session = requests.Session()
    form_data = {
        'vNUMPAG': '1', # 1 is 'Todos' in GeneXus state
        'GXState': '{"vNUMPAG":"1"}'
    }
    
    records = []
    try:
        res = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False, timeout=30)
        # Parse all company names from raw HTML & GXState
        state_matches = pd.read_html(res.text) if '<table' in res.text else []
        for df_table in state_matches:
            for col in df_table.columns:
                for val in df_table[col].dropna():
                    sval = str(val).strip()
                    if ('SOFOM' in sval or 'S.A.' in sval or 'S.A.P.I.' in sval) and len(sval) > 8:
                        if sval not in records:
                            records.append(sval)
    except Exception as e:
        print(f"[-] Error obteniendo CONDUSEF directo: {e}")
        
    return records

def firecrawl_crawl_asofom_and_sofomes():
    print("[*] Iniciando Crawl masivo en Firecrawl para ASOFOM y Sofomes.com...")
    crawl_url = "https://api.firecrawl.dev/v1/crawl"
    
    targets = [
        {"url": "https://asofom.mx/", "limit": 100},
        {"url": "https://sofomes.com/lista-sofomes-mexico", "limit": 100}
    ]
    
    extracted_mds = []
    for t in targets:
        print(f"[*] Iniciando job de Crawl en {t['url']} (límite {t['limit']} páginas)...")
        try:
            res = requests.post(crawl_url, json={"url": t["url"], "limit": t["limit"]}, headers=HEADERS, timeout=30)
            if res.status_code == 200:
                job_id = res.json().get("id")
                print(f"[+] Job iniciado exitosamente con ID: {job_id}")
                
                # Poll for completion
                status_url = f"https://api.firecrawl.dev/v1/crawl/status/{job_id}"
                for _ in range(30): # wait up to 2.5 mins per crawl
                    time.sleep(5)
                    st_res = requests.get(status_url, headers=HEADERS, timeout=15)
                    if st_res.status_code == 200:
                        st_data = st_res.json()
                        status = st_data.get("status")
                        completed = st_data.get("completed", 0)
                        total = st_data.get("total", 0)
                        print(f"    -> Estado Crawl: {status} ({completed}/{total} páginas procesadas)")
                        if status == "completed":
                            data = st_data.get("data", [])
                            for page in data:
                                extracted_mds.append(page.get("markdown", ""))
                            break
            else:
                print(f"[-] Error HTTP iniciando crawl {res.status_code}: {res.text[:200]}")
        except Exception as e:
            print(f"[-] Excepción durante crawl: {e}")
            
    return extracted_mds

if __name__ == "__main__":
    condusef_list = extract_condusef_full_catalog()
    print(f"[+] Registros encontrados en CONDUSEF: {len(condusef_list)}")
    
    firecrawl_docs = firecrawl_crawl_asofom_and_sofomes()
    print(f"[+] Páginas extraídas vía Firecrawl Crawl Job: {len(firecrawl_docs)}")
    
    # Save output
    output_path = "c:/Users/Antonio/.gemini/antigravity-ide/scratch/intelligential/data/full_scraped_directories.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({
            "condusef_companies": condusef_list,
            "crawled_pages_count": len(firecrawl_docs),
            "raw_docs_sample": [d[:500] for d in firecrawl_docs[:10]]
        }, f, ensure_ascii=False, indent=2)
        
    print(f"[🚀] PROCESO FINALIZADO. Datos completos guardados en: {output_path}")
