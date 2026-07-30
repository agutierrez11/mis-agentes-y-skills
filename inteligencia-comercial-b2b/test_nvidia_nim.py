import os
import sys
import requests
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv(dotenv_path="c:\\Users\\Antonio\\.gemini\\antigravity-ide\\scratch\\.env")

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

def call_nvidia_nim(prompt: str, model: str = "deepseek-ai/deepseek-r1"):
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.6,
        "max_tokens": 512
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

if __name__ == "__main__":
    print("Probando la API de NVIDIA NIM con DeepSeek-R1...")
    res = call_nvidia_nim("Responde en 1 frase: ¿Cuál es la principal diferencia entre Intelligential y Mambu en México?")
    print("\n--- Respuesta de NVIDIA NIM ---")
    print(res)
