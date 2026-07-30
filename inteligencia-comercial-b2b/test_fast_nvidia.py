import os
import sys
import requests
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv(dotenv_path="c:\\Users\\Antonio\\.gemini\\antigravity-ide\\scratch\\.env")

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

def test_fast_nvidia_models():
    # Probar modelos alternativos súper rápidos en NVIDIA NIM
    candidate_models = [
        "meta/llama-3.1-70b-instruct",
        "nvidia/nemotron-4-340b-instruct",
        "mistralai/mistral-large-2-instruct",
        "qwen/qwen2.5-72b-instruct"
    ]
    
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }
    
    for model in candidate_models:
        print(f"Probando {model}...")
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": "Responde en 1 frase corta: ¿Qué es una SOFOM en México?"}],
            "temperature": 0.5,
            "max_tokens": 100
        }
        res = requests.post(url, headers=headers, json=payload)
        if res.status_code == 200:
            print(f"\n✅ ¡ÉXITO CON {model}!")
            print("Respuesta:", res.json()["choices"][0]["message"]["content"])
            return model
        else:
            print(f"❌ {model} respondió {res.status_code}")
    return None

if __name__ == "__main__":
    test_fast_nvidia_models()
