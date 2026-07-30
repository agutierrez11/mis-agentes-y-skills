import os
import sys
import requests
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv(dotenv_path="c:\\Users\\Antonio\\.gemini\\antigravity-ide\\scratch\\.env")

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

def list_nvidia_models():
    url = "https://integrate.api.nvidia.com/v1/models"
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Accept": "application/json"
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        models = [m["id"] for m in res.json()["data"]]
        print(f"✅ Se encontraron {len(models)} modelos disponibles en NVIDIA NIM.")
        print("Primeros 10 modelos:")
        for m in models[:10]:
            print(f"  - {m}")
        return models
    else:
        print(f"❌ Error al listar modelos: {res.status_code} - {res.text}")
        return []

if __name__ == "__main__":
    list_nvidia_models()
