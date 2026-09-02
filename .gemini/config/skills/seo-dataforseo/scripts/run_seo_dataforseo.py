import os, sys, argparse, json, urllib.request, base64

def dataforseo_serp_live(keyword, login=None, password=None):
    """
    Integración oficial con DataForSEO v3 API (https://github.com/dataforseo/dataforseo-client-python)
    """
    user = login or os.getenv("DATAFORSEO_LOGIN")
    pwd = password or os.getenv("DATAFORSEO_PASSWORD")
    
    if not user or not pwd:
        return {
            "Status": "CREDENTIALS_REQUIRED",
            "Repo": "https://github.com/dataforseo/dataforseo-client-python",
            "Message": "Se requieren DATAFORSEO_LOGIN y DATAFORSEO_PASSWORD."
        }
    
    creds = base64.b64encode(f"{user}:{pwd}".encode()).decode()
    url = "https://api.dataforseo.com/v3/serp/google/organic/live/advanced"
    payload = json.dumps([{"keyword": keyword, "location_code": 2484, "language_code": "es"}]).encode()
    
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Basic {creds}",
        "Content-Type": "application/json"
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return json.loads(res.read().decode("utf-8"))
    except Exception as e:
        return {"Status": "Error", "Error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--keyword", required=True)
    args = parser.parse_args()
    print(json.dumps(dataforseo_serp_live(args.keyword), indent=2))
