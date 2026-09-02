import os
import sys
import argparse
import re
import urllib.parse
import urllib.request
import json
from bs4 import BeautifulSoup

def fetch_public_posts_and_icebreakers(target_name, domain=None):
    """
    Motor funcional agnóstico para monitorear publicaciones públicas y generar 'Icebreakers' (rompehielos de prospección).
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    posts_found = []
    
    # 1. Monitoreo de noticias y comunicados públicos del sitio web
    if domain:
        url = f"https://{domain}" if not domain.startswith('http') else domain
        for path in ['', '/noticias', '/blog', '/comunicados', '/prensa']:
            try:
                req = urllib.request.Request(f"{url}{path}", headers=headers)
                with urllib.request.urlopen(req, timeout=5) as res:
                    html = res.read().decode('utf-8', errors='ignore')
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Buscar artículos o párrafos con fechas/titulares
                    for item in soup.find_all(['h2', 'h3', 'article', 'p']):
                        txt = item.get_text().strip()
                        if 25 < len(txt) < 180 and any(w in txt.lower() for w in ['estación', 'gasolina', 'combustible', 'inauguración', 'premio', 'cre', 'sat', 'anexo', 'servicio', 'cliente', 'tecnología']):
                            posts_found.append(txt)
            except Exception:
                pass

    # Eliminar duplicados
    posts_clean = list(set(posts_found))[:5]
    
    # Generar rompehielos para prospección B2B
    icebreakers = []
    for p in posts_clean:
        icebreakers.append(f"Felicidades por su reciente comunicado sobre '{p[:60]}...'. En PayMind nos alineamos a esa misma visión...")
        
    if not icebreakers:
        icebreakers.append(f"Hola team de {target_name}, estuve revisando las innovaciones de sus estaciones de servicio y su presencia digital...")

    return {
        "Target": target_name,
        "Domain": domain,
        "Public_Posts_Detected": posts_clean,
        "Generated_Icebreakers": icebreakers,
        "Search_Dorks_For_LinkedIn_Posts": [
            f'site:linkedin.com/posts/ "{target_name}"',
            f'site:facebook.com "{target_name}" "publicación"'
        ]
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Public Posts & Social Media Icebreaker Engine")
    parser.add_argument("--target", required=True, help="Nombre de la empresa o directivo")
    parser.add_argument("--domain", help="Dominio web institucional")
    
    args = parser.parse_args()
    print(f"=== PUBLIC POSTS MONITOR & ICEBREAKER SKILL: {args.target} ===")
    res = fetch_public_posts_and_icebreakers(args.target, args.domain)
    print(json.dumps(res, indent=2, ensure_ascii=False))
