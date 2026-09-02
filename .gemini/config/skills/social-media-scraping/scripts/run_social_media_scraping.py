import os
import sys
import argparse
import re
import urllib.parse
import urllib.request
import json
from bs4 import BeautifulSoup

def scrape_social_media_profiles(target, domain=None, platform='all'):
    """
    Motor funcional agnóstico para extracción y rastreo de redes sociales de empresas o ejecutivos.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    results = {
        'Target': target,
        'Domain': domain,
        'Social_Links_Found': {},
        'Search_Queries': []
    }
    
    platforms = ['linkedin', 'facebook', 'twitter', 'instagram'] if platform == 'all' else [platform.lower()]
    
    # 1. Rastrear dominio objetivo si se proporciona
    if domain:
        url = f"https://{domain}" if not domain.startswith('http') else domain
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=5) as response:
                html = response.read().decode('utf-8', errors='ignore')
                soup = BeautifulSoup(html, 'html.parser')
                
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    for p in platforms:
                        if p in href.lower() and p not in results['Social_Links_Found']:
                            results['Social_Links_Found'][p] = href
        except Exception:
            pass

    # 2. Generar dorks de búsqueda para perfiles no encontrados
    for p in platforms:
        if p not in results['Social_Links_Found']:
            query = f'site:{p}.com "{target}"'
            results['Search_Queries'].append({
                'Platform': p,
                'Query': query,
                'Search_URL': f'https://www.google.com/search?q={urllib.parse.quote(query)}'
            })
            
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Social Media Scraping Engine Funcional')
    parser.add_argument('--target', required=True, help='Nombre de la empresa o persona objetivo')
    parser.add_argument('--domain', help='Dominio web oficial (opcional)')
    parser.add_argument('--platform', default='all', choices=['all', 'linkedin', 'facebook', 'twitter', 'instagram'], help='Plataforma específica')
    
    args = parser.parse_args()
    print(f"=== SOCIAL MEDIA SCRAPING SKILL: {args.target} ===")
    res = scrape_social_media_profiles(args.target, args.domain, args.platform)
    print(json.dumps(res, indent=2, ensure_ascii=False))
