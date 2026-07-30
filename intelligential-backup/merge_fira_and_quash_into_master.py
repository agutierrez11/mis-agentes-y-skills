import os
import re
import pandas as pd

def main():
    print("=== FUSION DEL PADRON FIRA BANXICO Y CLIENTES QUASH EN CAPA 4 DEL DATASET MASTER ===")
    
    main_csv = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\data\pipeline_real_sofomes_mx.csv"
    df_master = pd.read_csv(main_csv)
    
    # 1. Parse FIRA Markdown Raw
    fira_md = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\fira_sofomes_raw.md"
    fira_rows = []
    
    if os.path.exists(fira_md):
        with open(fira_md, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for l in lines:
                if l.startswith('|') and 'Intermediario Financiero' not in l and '---' not in l:
                    parts = [p.strip() for p in l.split('|')[1:-1]]
                    if len(parts) >= 5:
                        nombre = parts[0]
                        direccion = parts[1]
                        telefono = parts[2]
                        url_match = re.search(r'\((http[s]?://[^\)]+)\)', parts[3]) or re.search(r'\[([^\]]+)\]', parts[3])
                        url = url_match.group(1) if url_match else parts[3]
                        if not url.startswith('http'):
                            url = 'http://' + url
                            
                        fira_rows.append({
                            'denominacion_social_real': nombre + " (FIRA Acreditada / Fondeo Estatal)",
                            'estado_republica_sede': direccion.split(',')[-2].strip() if ',' in direccion else 'México',
                            'cartera_estimada_mrp': '$150M - $500M MXN (FIRA)',
                            'competidor_actual': 'Sistema Legado / FIRA Core',
                            'tier_pricing': 'Tier 2 ($80,000/mes)',
                            'estatus_funnel': '1. Por Contactar',
                            'sitio_web_oficial': url,
                            'tecnologias_detectadas': f'FIRA Intermediario / Tel: {telefono}'
                        })

    # 2. Quash.ai Customers Target
    quash_targets = [
        {'denominacion_social_real': 'Asefimex (Cliente Quash.ai Target)', 'sitio_web_oficial': 'https://www.asefimex.com/', 'tecnologias_detectadas': 'Quash.ai Credit Scoring / Core Pendiente'},
        {'denominacion_social_real': 'Crediavance (Cliente Quash.ai Target)', 'sitio_web_oficial': 'https://www.crediavance.com.mx/', 'tecnologias_detectadas': 'Quash.ai Credit Scoring / Core Pendiente'},
        {'denominacion_social_real': 'CrediCapital (Cliente Quash.ai Target)', 'sitio_web_oficial': 'https://www.credicapital.com.mx/', 'tecnologias_detectadas': 'Quash.ai Credit Scoring / Core Pendiente'},
        {'denominacion_social_real': 'Finamigo (Cliente Quash.ai Target)', 'sitio_web_oficial': 'https://finamigo.com.mx/', 'tecnologias_detectadas': 'Quash.ai Credit Scoring / Core Pendiente'},
        {'denominacion_social_real': 'Banco Bancrea (Cliente Quash.ai Target)', 'sitio_web_oficial': 'https://www.bancrea.com/', 'tecnologias_detectadas': 'Quash.ai Credit Scoring / Core Pendiente'}
    ]

    df_fira = pd.DataFrame(fira_rows)
    df_quash = pd.DataFrame(quash_targets)

    df_updated = pd.concat([df_master, df_fira, df_quash], ignore_index=True).drop_duplicates(subset=['sitio_web_oficial'])
    df_updated.to_csv(main_csv, index=False)
    
    print(f"[OK] Padron FIRA ({len(df_fira)} entidades) y Clientes Quash ({len(df_quash)} entidades) incorporados a Capa 4.")
    print(f"[OK] Total del Dataset Master Maestro actualizado: {len(df_updated)} Entidades Financieras.")

if __name__ == '__main__':
    main()
