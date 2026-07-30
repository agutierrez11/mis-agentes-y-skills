# ==============================================================================
# RADAR DE SEÑALES EN GOOGLE & LINKEDIN (100% GRATIS - SIN SALES NAVIGATOR)
# ==============================================================================
# Usa Google Search Dorks / Scraping directo con Lightpanda / Firecrawl
# Busca vacantes públicas y publicaciones de señales en SOFOMes de México
# ==============================================================================

import json
import urllib.parse
import urllib.request
import pandas as pd

KEYWORDS_RADAR = [
    "Integración Mambu",
    "Programador Buró de Crédito",
    "Oficial de Cumplimiento PLD SOFOM",
    "Mesa de Control Crédito",
    "Desarrollador Core Bancario",
    "API KYC Nufi Moffin"
]

def generate_google_linkedin_dorks():
    """Genera URLs de Google Dorks para escanear LinkedIn 100% Gratis"""
    print("=== 🛰️ GENERADOR DE RADAR LINKEDIN GRATUITO (DORKS) ===")
    results = []
    
    for kw in KEYWORDS_RADAR:
        # Dork para buscar vacantes/posts en LinkedIn México sin pagar Sales Navigator
        dork_query = f'site:linkedin.com/jobs OR site:linkedin.com/posts "{kw}" "México"'
        encoded_query = urllib.parse.quote(dork_query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        
        results.append({
            "keyword": kw,
            "dork_query": dork_query,
            "google_search_link": search_url,
            "senial_detectada": f"Empresa buscando resolver {kw}"
        })
        print(f"👉 Alerta para '{kw}': {search_url}\n")
        
    return results

if __name__ == "__main__":
    dorks = generate_google_linkedin_dorks()
    print(f"✅ Radar generado con {len(dorks)} filtros de señales operativas.")
