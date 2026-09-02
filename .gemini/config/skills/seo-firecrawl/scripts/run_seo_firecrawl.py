import os, sys, argparse, json, urllib.request

def firecrawl_scrape(url, api_key=None):
    """
    Integración oficial con Firecrawl API (MendableAI / Firecrawl GitHub Repo).
    https://github.com/mendableai/firecrawl
    """
    key = api_key or os.getenv("FIRECRAWL_API_KEY")
    if not key:
        return {
            "Status": "API_KEY_REQUIRED",
            "Message": "Configura FIRECRAWL_API_KEY o usa --api-key. Repositorio: https://github.com/mendableai/firecrawl",
            "Command_Fallback": f"npx -y firecrawl-cli scrape {url}"
        }
    
    endpoint = "https://api.firecrawl.dev/v1/scrape"
    payload = json.dumps({"url": url, "formats": ["markdown", "links"]}).encode("utf-8")
    req = urllib.request.Request(endpoint, data=payload, headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    })
    
    try:
        with urllib.request.urlopen(req, timeout=15) as res:
            data = json.loads(res.read().decode("utf-8"))
            return data
    except Exception as e:
        return {"Status": "Error", "Error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Firecrawl SEO Scraper (https://github.com/mendableai/firecrawl)")
    parser.add_argument("--url", required=True, help="URL a extraer en Markdown")
    parser.add_argument("--api-key", help="API Key de Firecrawl")
    args = parser.parse_args()
    print(json.dumps(firecrawl_scrape(args.url, args.api_key), indent=2, ensure_ascii=False))
