import os
import sys
import argparse
import urllib.parse
import urllib.request
import json
from bs4 import BeautifulSoup

def execute_osint_market_recon(target_domain_or_name):
    """
    Herramienta OSINT de Investigación de Mercado basada en SpiderFoot, theHarvester y Wappalyzer.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    domain = target_domain_or_name.replace('https://', '').replace('http://', '').split('/')[0]
    
    recon_results = {
        'Target': target_domain_or_name,
        'Domain': domain,
        'Tech_Stack_Detected': [],
        'OSINT_Tool_Equivalents': {
            'SpiderFoot': f'https://github.com/smicallef/spiderfoot (Análisis de huella corporativa 360°)',
            'Sherlock': f'https://github.com/sherlock-project/sherlock (Rastreo de usuarios en 400+ redes)',
            'theHarvester': f'https://github.com/laramies/theHarvester (Cosecha de subdominios y correos)',
            'Wappalyzer': f'https://github.com/wappalyzer/wappalyzer (Detección de ERP / CMS / Tech Stack)'
        },
        'Dorks_Investigacion_Mercado': [
            f'site:{domain} filetype:pdf (Documentos públicos, estados financieros o manuales)',
            f'site:{domain} "Odoo" OR "SAP" OR "ControlGAS" (Identificación de software interno)',
            f'site:linkedin.com/company "{domain}" (Perfil corporativo e infraestructura)'
        ]
    }
    
    # Inspección en vivo del Tech Stack (Wappalyzer / BuiltWith libre)
    try:
        req = urllib.request.Request(f"https://{domain}", headers=headers)
        with urllib.request.urlopen(req, timeout=5) as res:
            html = res.read().decode('utf-8', errors='ignore')
            
            # Detectar tecnologías comunes
            if 'wp-content' in html:
                recon_results['Tech_Stack_Detected'].append('WordPress CMS')
            if 'odoo' in html.lower() or 'web/static' in html:
                recon_results['Tech_Stack_Detected'].append('Odoo ERP')
            if 'elementor' in html:
                recon_results['Tech_Stack_Detected'].append('Elementor Builder')
            if 'bootstrap' in html.lower():
                recon_results['Tech_Stack_Detected'].append('Bootstrap UI')
            if 'google-analytics' in html or 'gtag' in html:
                recon_results['Tech_Stack_Detected'].append('Google Analytics')
    except Exception:
        pass
        
    return recon_results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="OSINT Recon Arsenal - Investigación de Mercado")
    parser.add_argument("--target", required=True, help="Dominio o nombre de la empresa a auditar")
    
    args = parser.parse_args()
    print(f"=== OSINT RECON ARSENAL: {args.target} ===")
    res = execute_osint_market_recon(args.target)
    print(json.dumps(res, indent=2, ensure_ascii=False))
