import os, sys, argparse, json

def get_free_ai_providers():
    """
    Directorio oficial y enrutador de modelos gratuitos (https://itsfree.ai/).
    """
    providers = {
        "Google_AI_Studio": {
            "Quota": "1,500 peticiones / día GRATIS",
            "Context": "1M tokens (Lectura de PDFs gigantes y video)",
            "Base_URL": "https://generativelanguage.googleapis.com/v1beta/openai/",
            "Requisitos": "Email de Google, sin tarjeta de crédito",
            "Mejor_Para": "Análisis documental de normativas, Anexo 30 SAT y contratos"
        },
        "Groq": {
            "Quota": "1,000 peticiones / día GRATIS",
            "Context": "131K tokens (Velocidad LPU extrema)",
            "Base_URL": "https://api.groq.com/openai/v1",
            "Requisitos": "Registro gratuito, sin tarjeta",
            "Mejor_Para": "Clasificación ultrarrápida de leads y extracción de contactos"
        },
        "NVIDIA_NIM": {
            "Quota": "40 peticiones / minuto GRATIS",
            "Context": "Hasta 1M tokens (82 modelos abiertos)",
            "Base_URL": "https://integrate.api.nvidia.com/v1",
            "Requisitos": "Verificación telefónica, sin tarjeta",
            "Mejor_Para": "Modelos especializados DeepSeek R1, Llama 3.3 y Nemotron"
        },
        "Cerebras": {
            "Quota": "1 Millón de tokens / día GRATIS",
            "Context": "65K tokens (Wafer-scale engine)",
            "Base_URL": "https://api.cerebras.ai/v1",
            "Requisitos": "Cuenta gratuita",
            "Mejor_Para": "Generación masiva de correos y secuencias de prospección"
        }
    }
    return {
        "Directory_Source": "https://itsfree.ai",
        "Total_Free_Providers_Documented": len(providers),
        "Recommended_Providers": providers
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Free LLM API Router (itsfree.ai)")
    parser.add_argument("--action", default="list", choices=["list", "route"], help="Acción a realizar")
    args = parser.parse_args()
    print(json.dumps(get_free_ai_providers(), indent=2, ensure_ascii=False))
