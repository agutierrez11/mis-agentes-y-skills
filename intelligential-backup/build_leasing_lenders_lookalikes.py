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
    print("=== ESCANEO MASIVO MULTI-QUERY DE LEASING MAQUINARIA & LENDERS DIGITALES EN MÉXICO ===")
    api_key = FIRECRAWL_API_KEY

    queries_leasing = [
        "arrendamiento puro maquinaria pesada mexico sofom",
        "arrendadora financiera equipo industrial mexico",
        "leasing vehicular flotillas empresas mexico",
        "arrendamiento equipo medico hospitalario mexico",
        "arrendamiento maquinaria agricola tractores mexico",
        "arrendadoras independientes equipo pesado mexico",
        "sofom leasing bajio queretaro leon mexico",
        "sofom leasing norte monterrey chihuahua mexico",
        "sofom leasing merida yucatan sur mexico",
        "factoraje financiero leasing sofom mexico",
        "directorio amsofac arrendadoras financieras mexico",
        "directorio amdm distribuidores maquinaria mexico leasing"
    ]

    queries_lenders = [
        "lenders digitales credito pyme mexico fintech",
        "plataformas credito digital pyme sofom mexico",
        "fintech credito empresarial factoring mexico",
        "neobancos credito corporativo mexico",
        "credito pyme online fintech mexico",
        "financieras digitales prestamos pyme mexico"
    ]

    leasing_list = []
    print("\n--- Extrayendo Universo Completo de Arrendadoras de Maquinaria & Equipo ---")
    for q in queries_leasing:
        print(f"Buscando: '{q}'...")
        res = search_firecrawl(q, api_key, limit=20)
        if res and res.get('success') and res.get('data'):
            for item in res['data']:
                url = item.get('url', '')
                title = item.get('title', '')
                desc = item.get('description', '')
                if 'gob.mx' not in url and 'wikipedia' not in url and 'facebook' not in url and 'youtube' not in url:
                    leasing_list.append({
                        'nicho': 'Leasing Maquinaria & Equipo',
                        'denominacion': title.split('|')[0].split('-')[0].strip(),
                        'sitio_web': url,
                        'descripcion': desc,
                        'categoria': 'Arrendamiento Heavy Equipment / Industrial'
                    })
        time.sleep(0.3)

    lenders_list = []
    print("\n--- Extrayendo Universo Completo de Lenders Digitales & Fintechs ---")
    for q in queries_lenders:
        print(f"Buscando: '{q}'...")
        res = search_firecrawl(q, api_key, limit=20)
        if res and res.get('success') and res.get('data'):
            for item in res['data']:
                url = item.get('url', '')
                title = item.get('title', '')
                desc = item.get('description', '')
                if 'gob.mx' not in url and 'wikipedia' not in url and 'facebook' not in url and 'youtube' not in url:
                    lenders_list.append({
                        'nicho': 'Lenders Digitales / Fintechs',
                        'denominacion': title.split('|')[0].split('-')[0].strip(),
                        'sitio_web': url,
                        'descripcion': desc,
                        'categoria': 'Crédito Digital Pyme / Fintech'
                    })
        time.sleep(0.3)

    df_leasing = pd.DataFrame(leasing_list).drop_duplicates(subset=['sitio_web'])
    df_lenders = pd.DataFrame(lenders_list).drop_duplicates(subset=['sitio_web'])

    df_leasing.to_csv(r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\data\lista_real_leasing_maquinaria.csv", index=False)
    df_lenders.to_csv(r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\data\lista_real_lenders_digitales.csv", index=False)

    print(f"\n[OK] Universo de Leasing Maquinaria ampliado a {len(df_leasing)} empresas reales.")
    print(f"[OK] Universo de Lenders Digitales ampliado a {len(df_lenders)} empresas reales.")

if __name__ == '__main__':
    main()
