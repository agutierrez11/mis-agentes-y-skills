import os, sys, argparse, json, urllib.request

def profound_ai_perplexity_check(brand_query, api_key=None):
    """
    Auditoría real de visibilidad en Motores de IA (Generative Engine Optimization).
    """
    key = api_key or os.getenv("PERPLEXITY_API_KEY")
    if not key:
        return {
            "Status": "API_KEY_REQUIRED",
            "Message": "Configura PERPLEXITY_API_KEY para evaluar la recomendación de la marca en IA."
        }
    
    url = "https://api.perplexity.ai/chat/completions"
    payload = json.dumps({
        "model": "sonar",
        "messages": [{"role": "user", "content": f"¿Cuáles son las mejores opciones para {brand_query} en México?"}]
    }).encode()
    
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return json.loads(res.read().decode("utf-8"))
    except Exception as e:
        return {"Status": "Error", "Error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    args = parser.parse_args()
    print(json.dumps(profound_ai_perplexity_check(args.query), indent=2))
