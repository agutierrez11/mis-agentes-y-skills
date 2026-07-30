import os
import sys
import json
import urllib.request

FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY', 'fc-a826332a3caa44278ce22953865de09a')

def scrape_fira(api_key):
    url = "https://api.firecrawl.dev/v1/scrape"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "url": "https://fira.gob.mx/Nd/html/IF-sofom.html",
        "formats": ["markdown"],
        "onlyMainContent": True
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data
    except Exception as e:
        print(f"Error scraping FIRA: {e}")
        return None

def main():
    print("=== SCRAPING Y AUDITORÍA DEL PADRÓN FIRA ===")
    res = scrape_fira(FIRECRAWL_API_KEY)
    if res and res.get('success') and res.get('data'):
        markdown = res['data'].get('markdown', '')
        print("\n[OK] Contenido extraido de FIRA IF-sofom:")
        print("--------------------------------------------------")
        print(markdown[:2000])
        print("--------------------------------------------------")
        
        with open("fira_sofomes_raw.md", "w", encoding="utf-8") as f:
            f.write(markdown)
        print("[OK] Guardado en fira_sofomes_raw.md")

if __name__ == '__main__':
    main()
