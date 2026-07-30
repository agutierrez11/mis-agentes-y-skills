import os
import sys
import requests
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv(dotenv_path="c:\\Users\\Antonio\\.gemini\\antigravity-ide\\scratch\\.env")

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

def test_nvidia_models():
    # Modelos comunes en el catálogo de NVIDIA NIM
    candidate_models = [
        "meta/llama-3.3-70b-instruct",
        "nvidia/nemotron-4-340b-instruct",
        "deepseek-ai/deepseek-r1",
        "mistralai/mistral-large-2-instruct"
    ]
    
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }
    
    for model in candidate_models:
        print(f"Probando modelo: {model}...")
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": "Hola, responde brevemente."}],
            "temperature": 0.5,
            "max_tokens": 100
        }
        res = requests.post(url, headers=headers, json=payload)
        if res.status_code == 200:
            print(f"✅ ¡ÉXITO con {model}!")
            print("Respuesta:", res.json()["choices"][0]["message"]["content"])
            return model
        else:
            print(f"❌ Falló {model}: Status {res.status_code} - {res.text[:100]}")
    return None

if __name__ == "__main__":
    test_nvidia_models()
