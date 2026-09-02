import os, sys, argparse, json, urllib.request

def ahrefs_domain_rating(target_domain, api_key=None):
    """
    Integración oficial con Ahrefs v3 API (https://github.com/ahrefs/ahrefs-api-python)
    """
    key = api_key or os.getenv("AHREFS_API_KEY")
    if not key:
        return {
            "Status": "API_KEY_REQUIRED",
            "Repo": "https://github.com/ahrefs/ahrefs-api-python",
            "Message": "Se requiere AHREFS_API_KEY en variables de entorno o mediante --api-key"
        }
    
    url = f"https://api.ahrefs.com/v3/site-explorer/domain-rating?target={target_domain}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {key}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return json.loads(res.read().decode("utf-8"))
    except Exception as e:
        return {"Status": "Error", "Error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", required=True)
    parser.add_argument("--api-key")
    args = parser.parse_args()
    print(json.dumps(ahrefs_domain_rating(args.domain, args.api_key), indent=2))
