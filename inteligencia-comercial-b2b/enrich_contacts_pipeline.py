import json
import re
import urllib.parse

def generate_linkedin_xray_query(company_name):
    """
    Genera la consulta Google X-Ray para encontrar en LinkedIn al CEO, Director General, 
    Director de Operaciones u Oficial de Cumplimiento de la SOFOM.
    """
    clean_name = company_name.replace(", S.A. de C.V., SOFOM, E.N.R.", "").replace(", S.A.P.I. de C.V., SOFOM, E.N.R.", "").replace(", S.A. de C.V.", "").strip()
    
    roles = '("CEO" OR "Director General" OR "Director de Operaciones" OR "Director de Crédito" OR "Oficial de Cumplimiento")'
    query = f'site:linkedin.com/in/ {roles} "{clean_name}"'
    
    google_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    return query, google_url

def generate_email_patterns(first_name, last_name, domain):
    """
    Genera los patrones estándar de correo corporativo B2B validados para outbound.
    """
    fn = first_name.lower().strip()
    ln = last_name.lower().strip()
    d = domain.lower().strip()
    
    return [
        f"{fn}.{ln}@{d}",        # carlos.mendoza@empresa.mx
        f"{fn[0]}{ln}@{d}",       # cmendoza@empresa.mx
        f"{fn}@{d}",              # carlos@empresa.mx
        f"{fn}{ln[0]}@{d}",       # carlosm@empresa.mx
        f"contacto@{d}"           # fallback corporativo
    ]

if __name__ == "__main__":
    sample_sofom = "AB7 Servicios, S.A. de C.V., SOFOM, E.N.R."
    query, url = generate_linkedin_xray_query(sample_sofom)
    
    print("=== PIPELINE DE ENRIQUECIMIENTO DE CONTACTOS ===")
    print(f"Empresa: {sample_sofom}")
    print(f"Google X-Ray Query: {query}")
    print(f"URL de Búsqueda Directa: {url}")
    print("\nEjemplo de Patrones de Email (Carlos Mendoza @ ab7servicios.mx):")
    patterns = generate_email_patterns("Carlos", "Mendoza", "ab7servicios.mx")
    for p in patterns:
        print(f" - {p}")
