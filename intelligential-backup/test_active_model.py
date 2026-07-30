import os
import sys
import requests
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv(dotenv_path="c:\\Users\\Antonio\\.gemini\\antigravity-ide\\scratch\\.env")

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

def test_active_model():
    # Usando un modelo verificado de la lista oficial de NVIDIA NIM
    model_id = "deepseek-ai/deepseek-v4-flash"
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model_id,
        "messages": [
            {"role": "user", "content": "Responde en 1 frase: ¿Cuál es la ventaja de Intelligential frente a Mambu en México?"}
        ],
        "temperature": 0.6,
        "max_tokens": 150
    }
    
    print(f"Enviando consulta a NVIDIA NIM usando {model_id}...")
    res = requests.post(url, headers=headers, json=payload)
    if res.status_code == 200:
        print("\n✅ ¡ÉXITO! Respuesta de NVIDIA NIM:")
        print(res.json()["choices"][0]["message"]["content"])
    else:
        print(f"❌ Error {res.status_code}: {res.text}")

if __name__ == "__main__":
    test_active_model()
