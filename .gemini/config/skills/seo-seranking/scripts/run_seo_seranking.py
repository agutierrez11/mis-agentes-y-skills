import os, sys, argparse, json, urllib.request

def seranking_get_positions(site_id, api_token=None):
    """
    Integración oficial SE Ranking REST API v3 (https://github.com/seranking/seranking-api-python)
    """
    token = api_token or os.getenv("SERANKING_API_TOKEN")
    if not token:
        return {
            "Status": "TOKEN_REQUIRED",
            "Repo": "https://github.com/seranking/seranking-api-python",
            "Message": "Se requiere SERANKING_API_TOKEN."
        }
    
    url = f"https://api.seranking.com/v3/sites/{site_id}/positions"
    req = urllib.request.Request(url, headers={"Authorization": f"Token {token}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return json.loads(res.read().decode("utf-8"))
    except Exception as e:
        return {"Status": "Error", "Error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-id", required=True)
    args = parser.parse_args()
    print(json.dumps(seranking_get_positions(args.site_id), indent=2))
