import os
import sys
import argparse
import re
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

def extract_emails_from_url(url, depth=1, max_pages=10):
    """
    Crawler agnóstico de correos electrónicos desde una URL dada.
    """
    visited = set()
    to_visit = [url]
    found_emails = set()
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

    pages_crawled = 0
    while to_visit and pages_crawled < max_pages:
        curr_url = to_visit.pop(0)
        if curr_url in visited:
            continue
        visited.add(curr_url)
        pages_crawled += 1
        
        try:
            req = urllib.request.Request(curr_url, headers=headers)
            with urllib.request.urlopen(req, timeout=5) as response:
                html = response.read().decode('utf-8', errors='ignore')
                
                # Extraer correos
                emails = set(re.findall(email_pattern, html))
                found_emails.update(emails)
                
                # Buscar enlaces internos si profundidad > 1
                if depth > 1:
                    soup = BeautifulSoup(html, 'html.parser')
                    for a in soup.find_all('a', href=True):
                        link = a['href']
                        full_link = urllib.parse.urljoin(curr_url, link)
                        parsed_base = urllib.parse.urlparse(url).netloc
                        parsed_link = urllib.parse.urlparse(full_link).netloc
                        if parsed_base == parsed_link and full_link not in visited:
                            to_visit.append(full_link)
        except Exception:
            pass
            
    return list(found_emails)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Email Crawl Skill Agnóstica Universal')
    parser.add_argument('--url', required=True, help='URL objetivo a rastrear (ej: https://ejemplo.com)')
    parser.add_argument('--depth', type=int, default=2, help='Profundidad de navegación')
    parser.add_argument('--max-pages', type=int, default=10, help='Máximo de páginas a analizar')
    
    args = parser.parse_args()
    print(f"=== EMAIL CRAWL SKILL: Rastreando {args.url} (Profundidad: {args.depth}) ===")
    emails = extract_emails_from_url(args.url, args.depth, args.max_pages)
    print(f"Correos encontrados ({len(emails)}):")
    for email in emails:
        print(f" - {email}")
