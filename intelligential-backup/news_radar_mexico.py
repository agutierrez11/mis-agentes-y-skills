# ==============================================================================
# MOTOR DE BÚSQUEDA DE NOTICIAS DE CORE BANCARIO & FINTECH (100% MÉXICO-FIRST)
# ==============================================================================
# Escanea fuentes líderes (Iupana, Expansión, El Economista, Forbes MX, LinkedIn)
# Filtrado estricto para noticias, regulaciones CNBV y tendencias de Core en México
# ==============================================================================

import json
import urllib.parse
import urllib.request
import pandas as pd

# Fuentes verificadas con cobertura de regulación y tecnología bancaria en México
SOURCES_MEXICO = [
    "expansion.mx",
    "eleconomista.com.mx",
    "forbes.com.mx",
    "iupana.com",
    "milenio.com",
    "linkedin.com/posts"
]

# Temas clave que impactan al Core Bancario y SOFOMes en México
TOPICS_CORE_MX = [
    '("Core Bancario" OR "Core Financiero") "México"',
    '("CNBV" OR "SITI PLD") ("multa" OR "disposiciones" OR "inspección")',
    '("SOFOM" OR "Arrendadora") ("modernización" OR "sistemas" OR "tecnología")',
    '("Open Finance" OR "BaaS") "México" "regulación"',
    '("Inteligencia Artificial" OR "IA") "banca mexicana" OR "financiera"',
    '("SPEI" OR "pagos en tiempo real") "infraestructura" "México"'
]

def search_mexico_core_news():
    """Genera búsquedas dirigidas a fuentes clave filtradas exclusivamente para México"""
    print("=== 🇲🇽 MOTOR DE BÚSQUEDA DE NOTICIAS Y SEÑALES DE CORE BANCARIO EN MÉXICO ===")
    
    dorks_list = []
    
    for topic in TOPICS_CORE_MX:
        # Forzar filtro geográfico y de dominio
        sources_filter = " OR ".join([f"site:{src}" for src in SOURCES_MEXICO])
        full_query = f'({sources_filter}) {topic}'
        encoded_query = urllib.parse.quote(full_query)
        google_news_url = f"https://www.google.com/search?q={encoded_query}&tbs=qdr:m" # Filtro de noticias del último mes
        
        dorks_list.append({
            "topic": topic,
            "query": full_query,
            "search_url": google_news_url
        })
        print(f"📰 Noticia/Tendencia MX: {topic}")
        print(f"👉 URL Google News: {google_news_url}\n")
        
    return dorks_list

if __name__ == "__main__":
    results = search_mexico_core_news()
    print(f"✅ Motor de Noticias ejecutado: {len(results)} canales de inteligencia para México configurados.")
