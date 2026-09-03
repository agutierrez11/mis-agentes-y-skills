import os
import sys
import argparse
import json
import urllib.request
import re
from bs4 import BeautifulSoup

def crawl_and_clean_markdown(url):
    """
    Motor funcional Crawl4AI agnóstico (https://github.com/unclecode/crawl4ai).
    Extrae contenido web, elimina etiquetas superfluas y genera Markdown estructurado para LLMs.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as res:
            html = res.read().decode('utf-8', errors='ignore')
            
        soup = BeautifulSoup(html, 'html.parser')
        
        # Eliminar scripts, estilos, iframes y publicidad
        for element in soup(['script', 'style', 'noscript', 'iframe', 'svg', 'header', 'footer']):
            element.decompose()
            
        # Extraer metadatos
        title = soup.title.string.strip() if soup.title and soup.title.string else url
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        desc = meta_desc['content'].strip() if meta_desc and 'content' in meta_desc.attrs else ""
        
        # Extraer enlaces
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            txt = a.get_text().strip()
            if href.startswith('http') and len(txt) > 2:
                links.append({'text': txt, 'url': href})
                
        # Extraer correos y teléfonos
        text_content = soup.get_text(separator=' ')
        emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text_content)))
        phones = list(set(re.findall(r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text_content)))
        
        lines = [line.strip() for line in text_content.splitlines() if line.strip()]
        clean_markdown = " \n ".join(lines[:100])
        
        return {
            "Status": "Success",
            "URL": url,
            "Title": title,
            "Description": desc,
            "Contacts": {
                "Emails": emails,
                "Phones": phones[:5]
            },
            "Internal_Links_Count": len(links),
            "Markdown_Summary": clean_markdown[:1500]
        }
    except Exception as e:
        return {"Status": "Error", "URL": url, "Message": str(e)}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Crawl4AI Web Enrichment Engine")
    parser.add_argument("--url", required=True, help="URL a extraer y convertir en Markdown limpio")
    args = parser.parse_args()
    print(json.dumps(crawl_and_clean_markdown(args.url), indent=2, ensure_ascii=False))
