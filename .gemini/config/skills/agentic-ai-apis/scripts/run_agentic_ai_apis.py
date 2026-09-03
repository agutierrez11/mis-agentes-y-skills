import os, sys, argparse, json

API_CATALOG = {
    "mcp_servers": {
        "Descripcion": "Servidores Model Context Protocol (MCP) para dotar de herramientas al IDE y agentes.",
        "Top_Recomendados": [
            {"Nombre": "filesystem-mcp", "Uso": "Lectura y edición segura de archivos locales."},
            {"Nombre": "brave-search-mcp", "Uso": "Búsqueda web sin rastreo y sin bloqueos de IP."},
            {"Nombre": "postgres-mcp", "Uso": "Consultas directas a bases de datos relacionales."},
            {"Nombre": "github-mcp", "Uso": "Automatización de commits, branches y pull requests."},
            {"Nombre": "minimax-mcp", "Uso": "Generación de video y audio ultra-realista por tool call."}
        ]
    },
    "contact_and_enrichment_apis": {
        "Descripcion": "APIs para validación de datos corporativos, correos y decisores.",
        "Top_Recomendados": [
            {"Nombre": "Hunter.io API", "Uso": "Detección de patrones de correo corporativo por dominio."},
            {"Nombre": "ZeroBounce / Reacher", "Uso": "Verificación SMTP/DNS de correos sin enviar email."},
            {"Nombre": "Apollo.io API", "Uso": "Enriquecimiento de títulos de puesto y perfiles de LinkedIn."},
            {"Nombre": "Wappalyzer API", "Uso": "Detección remota de tecnologías, frameworks y pasarelas de pago."}
        ]
    },
    "messaging_and_delivery_apis": {
        "Descripcion": "APIs para envío y orquestación de mensajes.",
        "Top_Recomendados": [
            {"Nombre": "Resend API", "Uso": "Envío de correos transaccionales y de prospección con alta entregabilidad."},
            {"Nombre": "Meta WhatsApp Cloud API", "Uso": "Envío oficial de notificaciones y ligas de pago por WhatsApp."},
            {"Nombre": "Twilio API", "Uso": "SMS, verificación y telefonía programable."}
        ]
    },
    "free_computing_and_llms": {
        "Descripcion": "Endpoints y modelos de costo cero para enjambres masivos.",
        "Top_Recomendados": [
            {"Nombre": "Google AI Studio", "Limite": "1,500 req/día", "Ventana": "1M tokens"},
            {"Nombre": "Groq LPU", "Limite": "1,000 req/día", "Ventana": "131K tokens"},
            {"Nombre": "NVIDIA NIM", "Limite": "40 req/min", "Ventana": "Hasta 1M tokens (82 modelos)"}
        ]
    }
}

def query_catalog(category=None):
    if category and category in API_CATALOG:
        return API_CATALOG[category]
    return {
        "Catalogo_Referencia": "https://github.com/cporter202/agentic-ai-apis",
        "Total_Categorias": len(API_CATALOG),
        "Categorias": API_CATALOG
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Agentic AI APIs & MCP Catalog Explorer")
    parser.add_argument("--category", choices=["mcp_servers", "contact_and_enrichment_apis", "messaging_and_delivery_apis", "free_computing_and_llms"], help="Categoría a explorar")
    args = parser.parse_args()
    print(json.dumps(query_catalog(args.category), indent=2, ensure_ascii=False))
