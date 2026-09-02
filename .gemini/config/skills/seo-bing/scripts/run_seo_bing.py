import os, sys, argparse, json, urllib.request

def bing_get_url_submission_quota(site_url, api_key=None):
    """
    Integración oficial Bing Webmaster Tools API (https://github.com/microsoft/bing-webmaster-sdk)
    """
    key = api_key or os.getenv("BING_WEBMASTER_KEY")
    if not key:
        return {
            "Status": "API_KEY_REQUIRED",
            "Repo": "https://github.com/microsoft/bing-webmaster-sdk",
            "Message": "Se requiere BING_WEBMASTER_KEY."
        }
    
    url = f"https://ssl.bing.com/webmaster/api.svc/json/GetUrlSubmissionQuota?siteUrl={site_url}&apikey={key}"
    try:
        with urllib.request.urlopen(url, timeout=10) as res:
            return json.loads(res.read().decode("utf-8"))
    except Exception as e:
        return {"Status": "Error", "Error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", required=True)
    args = parser.parse_args()
    print(json.dumps(bing_get_url_submission_quota(args.site), indent=2))
