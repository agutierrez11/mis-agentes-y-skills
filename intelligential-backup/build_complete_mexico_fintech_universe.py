import os
import sys
import json
import time
import urllib.request
import pandas as pd

FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY', 'fc-a826332a3caa44278ce22953865de09a')

def search_firecrawl(query, api_key, limit=20):
    url = "https://api.firecrawl.dev/v1/search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "query": query,
        "limit": limit
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data
    except Exception as e:
        print(f"Error searching Firecrawl for '{query}': {e}")
        return None

def main():
    print("=== CONSTRUCCIÓN DEL UNIVERSO MAESTRO 100% REVOPS FINTECH MÉXICO ===")
    api_key = FIRECRAWL_API_KEY

    queries_sources = [
        # 1. SOCAPs & Cajas Populares
        ("SOCAPs Cajas Populares", "caja popular ahorro y prestamo mexico socap cnbv"),
        ("SOCAPs Cajas Populares", "cooperativa de ahorro y credito mexico socap regulada"),
        
        # 2. Uniones de Crédito CNBV
        ("Uniones de Crédito", "union de credito agricola industrial cnbv mexico"),
        ("Uniones de Crédito", "union de credito comercial financiera mexico"),
        
        # 3. Softcrédito & DynamiCore Lookalikes
        ("Softcrédito Clientes", "softcredito clientes sofom core bancario mexico"),
        ("DynamiCore Clientes", "dynamicore clientes sofom core bancario mexico"),
        ("MySys Clientes", "mysys sysde clientes sofom core bancario mexico"),
        
        # 4. Fleet Leasing & AMAVEC
        ("Fleet Leasing / Flotillas", "arrendadoras de flotillas vehiculos amavec mexico leasing"),
        ("Fleet Leasing / Flotillas", "arrendamiento automotriz puro leasing empresas mexico"),
        
        # 5. CMIC & AMDM Maquinaria Industrial
        ("Maquinaria Pesada Industrial", "arrendadoras de maquinaria de construccion cmic mexico"),
        ("Maquinaria Pesada Industrial", "distribuidores de maquinaria amdm leasing mexico")
    ]

    extracted_records = []
    
    for category_name, query in queries_sources:
        print(f"\nExtrayendo [{category_name}]: '{query}'...")
        res = search_firecrawl(query, api_key, limit=20)
        if res and res.get('success') and res.get('data'):
            for item in res['data']:
                url = item.get('url', '')
                title = item.get('title', '')
                desc = item.get('description', '')
                if 'gob.mx' not in url and 'wikipedia' not in url and 'facebook' not in url and 'youtube' not in url:
                    extracted_records.append({
                        'denominacion_social_real': title.split('|')[0].split('-')[0].strip() + f" ({category_name})",
                        'estado_republica_sede': 'Nacional / México',
                        'cartera_estimada_mrp': '$80M - $350M MXN',
                        'competidor_actual': 'Sistema Legado / In-House' if 'Clientes' not in category_name else category_name.replace(' Clientes', ''),
                        'tier_pricing': 'Tier 2 ($42,000/mes)',
                        'estatus_funnel': '1. Por Contactar',
                        'sitio_web_oficial': url,
                        'tecnologias_detectadas': category_name
                    })
        time.sleep(0.3)

    # Save to New Master CSV
    df_new = pd.DataFrame(extracted_records).drop_duplicates(subset=['sitio_web_oficial'])
    
    main_csv = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\data\pipeline_real_sofomes_mx.csv"
    df_main = pd.read_csv(main_csv)
    
    df_master = pd.concat([df_main, df_new], ignore_index=True).drop_duplicates(subset=['sitio_web_oficial'])
    df_master.to_csv(main_csv, index=False)

    print(f"\n[OK] ¡UNIVERSO MASTER DE FINTECH EN MÉXICO CONSTRUIDO CON ÉXITO!")
    print(f"[OK] Total de entidades en la Base de Datos Maestro: {len(df_master)} registros.")

if __name__ == '__main__':
    main()
