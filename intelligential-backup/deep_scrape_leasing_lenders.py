import os
import sys
import json
import time
import urllib.request
import pandas as pd

FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY', 'fc-a826332a3caa44278ce22953865de09a')

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
        print(f"Error scraping '{site_url}': {e}")
        return None

def extract_tech_stack(markdown_content):
    combined = str(markdown_content).lower()
    techs = []
    if 'aws' in combined or 'amazon' in combined: techs.append('AWS Cloud')
    if 'azure' in combined: techs.append('Microsoft Azure')
    if 'wordpress' in combined: techs.append('WordPress')
    if 'hubspot' in combined: techs.append('HubSpot CRM')
    if 'zendesk' in combined: techs.append('Zendesk')
    if 'mambu' in combined: techs.append('Mambu')
    if 'softcredito' in combined or 'softcrédito' in combined: techs.append('Softcrédito')
    if 'dynamicore' in combined: techs.append('DynamiCore')
    
    return ", ".join(techs) if techs else "Sistema Legado / In-House"

def main():
    print("=== DEEP FIRECRAWL SCRAPE EN TIEMPO REAL: 59 LEASING & LENDERS DIGITALES ===")
    api_key = FIRECRAWL_API_KEY
    
    main_csv = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\data\pipeline_real_sofomes_mx.csv"
    df = pd.read_csv(main_csv)
    
    target_mask = df['denominacion_social_real'].str.contains('Leasing Maquinaria|Lender Digital', case=False, na=False)
    target_rows = df[target_mask]
    
    print(f"Encontradas {len(target_rows)} entidades para deep scrape con Firecrawl...")
    
    scraped_count = 0
    for idx, row in target_rows.iterrows():
        url = str(row.get('sitio_web_oficial', ''))
        nombre = str(row.get('denominacion_social_real', ''))
        
        if url and 'http' in url and 'facebook' not in url and 'youtube' not in url and 'instagram' not in url:
            print(f"[{scraped_count+1}/{len(target_rows)}] Escaneando codigo completo de: {nombre} ({url})...")
            res = scrape_firecrawl(url, api_key)
            if res and res.get('success') and res.get('data'):
                markdown = res['data'].get('markdown', '')
                stack = extract_tech_stack(markdown)
                df.at[idx, 'tecnologias_detectadas'] = stack
                df.at[idx, 'competidor_actual'] = stack
                print(f"   [OK] Tech Detectada: {stack}\n")
            else:
                print("   [SKIP] Error al raspar sitio.\n")
        scraped_count += 1
        time.sleep(0.3)
        
    df.to_csv(main_csv, index=False)
    print(f"\n[OK] Deep Scrape completado en las {scraped_count} entidades. CSV actualizado.")

if __name__ == '__main__':
    main()
