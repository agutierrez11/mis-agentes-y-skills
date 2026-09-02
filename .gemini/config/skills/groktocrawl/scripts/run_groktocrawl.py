import os, sys, argparse, json, urllib.request, re

def groktocrawl_scrape(url, host="http://localhost:8080"):
    """
    Integración oficial con groktocrawl (https://github.com/groktopus/groktocrawl)
    Scraper self-hosted compatible con API de Firecrawl para cualquier proyecto.
    """
    try:
        req = urllib.request.Request(f"{host}/v1/scrape", data=json.dumps({"url": url}).encode(), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as res:
            return json.loads(res.read().decode())
    except Exception:
        # Fallback autónomo si el servidor local no está arriba
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=5) as res:
                html = res.read().decode('utf-8', errors='ignore')
                clean_text = re.sub(r'<[^>]+>', ' ', html)
                return {"Status": "Fallback_Local", "URL": url, "Content_Snippet": ' '.join(clean_text.split())[:500]}
        except Exception as e:
            return {"Status": "Error", "Error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Groktocrawl Universal Agent Scraper")
    parser.add_argument("--url", required=True, help="URL objetivo a extraer")
    parser.add_argument("--host", default="http://localhost:8080", help="Host de groktocrawl local")
    args = parser.parse_args()
    print(json.dumps(groktocrawl_scrape(args.url, args.host), indent=2, ensure_ascii=False))
