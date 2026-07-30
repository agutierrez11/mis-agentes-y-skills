import os
import sys
import json
import urllib.request
import pandas as pd

FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY', 'fc-a826332a3caa44278ce22953865de09a')

def scrape_efisys_customers(api_key):
    url = "https://api.firecrawl.dev/v1/scrape"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "url": "https://www.efisys.com.mx/customers.php",
        "formats": ["markdown"],
        "onlyMainContent": True
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data
    except Exception as e:
        print(f"Error scraping EFISYS: {e}")
        return None

def main():
    print("=== MOTOR LOOKALIKE EFISYS (RIP & REPLACE) ===")
    res = scrape_efisys_customers(FIRECRAWL_API_KEY)
    if res and res.get('success') and res.get('data'):
        markdown = res['data'].get('markdown', '')
        print("\n[OK] Contenido Markdown extraido de EFISYS Customers:")
        print("--------------------------------------------------")
        print(markdown[:1500])
        print("--------------------------------------------------")
        
        # Save output for inspection
        with open("efisys_customers_raw.md", "w", encoding="utf-8") as f:
            f.write(markdown)
        print("[OK] Guardado en efisys_customers_raw.md")

if __name__ == '__main__':
    main()
