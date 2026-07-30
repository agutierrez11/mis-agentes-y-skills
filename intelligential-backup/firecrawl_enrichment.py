import os
import sys
import json
import time
import urllib.request
import pandas as pd

FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY', 'fc-a826332a3caa44278ce22953865de09a')

def search_firecrawl(query, api_key):
    url = "https://api.firecrawl.dev/v1/search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "query": query,
        "limit": 2
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data
    except Exception as e:
        print(f"Error calling Firecrawl Search: {e}")
        return None

def scrape_firecrawl(site_url, api_key):
    url = "https://api.firecrawl.dev/v1/scrape"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "url": site_url,
        "formats": ["markdown"],
        "onlyMainContent": True
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data
    except Exception as e:
        print(f"Error calling Firecrawl Scrape for '{site_url}': {e}")
        return None

def extract_tech_details(site_url, search_snippet, markdown_content):
    combined = (str(site_url) + " " + str(search_snippet) + " " + str(markdown_content)).lower()
    
    technologies = []
    if 'dynamicore' in combined:
        technologies.append('DynamiCore')
    if 'softcredito' in combined or 'softcrédito' in combined:
        technologies.append('Softcrédito')
    if 'ascendes' in combined:
        technologies.append('Ascendes')
    if 'mambu' in combined:
        technologies.append('Mambu')
    if 'aws' in combined or 'amazon' in combined:
        technologies.append('AWS Cloud')
    if 'azure' in combined:
        technologies.append('Microsoft Azure')
    if 'wordpress' in combined:
        technologies.append('WordPress')
    if 'react' in combined:
        technologies.append('React.js')
    if 'hubspot' in combined:
        technologies.append('HubSpot CRM')
    if 'zendesk' in combined:
        technologies.append('Zendesk')

    if technologies:
        return ", ".join(technologies)
    else:
        return "Sistema Legado / In-House"

def main():
    print("=== FIRECRAWL MASS ENRICHMENT BATCH: 600 CORE SOFOMES ===")
    api_key = FIRECRAWL_API_KEY
    if not api_key:
        print("Error: No Firecrawl API key provided.")
        sys.exit(1)
        
    csv_path = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\data\pipeline_real_sofomes_mx.csv"
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        sys.exit(1)
        
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} SOFOMes from dataset.")
    
    if 'sitio_web_oficial' not in df.columns:
        df['sitio_web_oficial'] = ''
    if 'tecnologias_detectadas' not in df.columns:
        df['tecnologias_detectadas'] = ''
        
    processed = 0
    max_to_process = 600
    
    for idx, row in df.head(max_to_process).iterrows():
        nombre_raw = str(row.get('denominacion_social_real', '')).split(',')[0]
        site_url = str(row.get('sitio_web_oficial', ''))
        
        # Step 1: Find URL if missing
        if not site_url or site_url == 'nan' or 'condusef' in site_url or 'facebook' in site_url:
            query = f"SOFOM {nombre_raw} Mexico sitio oficial"
            print(f"[{idx+1}/{max_to_process}] 1. Buscando URL: {nombre_raw}...")
            search_res = search_firecrawl(query, api_key)
            if search_res and search_res.get('success') and search_res.get('data'):
                site_url = search_res['data'][0].get('url', '')
                snippet = search_res['data'][0].get('description', '')
                df.at[idx, 'sitio_web_oficial'] = site_url
            else:
                snippet = ''
        else:
            snippet = ''

        # Step 2: Scrape URL to extract full technographic stack
        markdown_text = ""
        if site_url and 'http' in site_url and 'condusef' not in site_url and 'facebook' not in site_url:
            print(f"[{idx+1}/{max_to_process}] 2. Escaneando Tecnologías de: {site_url}...")
            scrape_res = scrape_firecrawl(site_url, api_key)
            if scrape_res and scrape_res.get('success') and scrape_res.get('data'):
                markdown_text = scrape_res['data'].get('markdown', '')
                
        # Detect Tech Stack
        stack = extract_tech_details(site_url, snippet, markdown_text)
        df.at[idx, 'competidor_actual'] = stack
        df.at[idx, 'tecnologias_detectadas'] = stack
        
        print(f"   [OK] Site: {site_url}")
        print(f"   [OK] Tech: {stack}\n")
        processed += 1
        
        # Save progress checkpoint every 50 records
        if processed % 50 == 0:
            df.to_csv(csv_path, index=False)
            print(f"--- CHECKPOINT INTERMEDIO: {processed} SOFOMes guardadas en CSV ---\n")
            
        time.sleep(0.15)

    # Save final CSV
    df.to_csv(csv_path, index=False)
    print(f"\n[OK] Enriquecimiento Masivo de 600 SOFOMes finalizado exitosamente. {processed} entidades guardadas.")

if __name__ == '__main__':
    main()
