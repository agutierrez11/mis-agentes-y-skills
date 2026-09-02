import os
import sys
import argparse
import urllib.parse
import urllib.request
import json

def osint_dossier_search(name_or_company, domain=None):
    """
    Motor OSINT agnóstico para búsqueda de huellas digitales de ejecutivos y empresas.
    """
    dossier = {
        'Target': name_or_company,
        'Domain': domain,
        'LinkedIn_Search_Query': f'site:linkedin.com/in/ "{name_or_company}"',
        'Google_Dorks': [
            f'"{name_or_company}" "contacto" OR "celular" OR "directorio"',
            f'site:gob.mx "{name_or_company}"',
            f'"{domain}" "correo" OR "email" OR "telefono"' if domain else None
        ],
        'Registros_Publicos': [
            f'https://www.google.com/search?q={urllib.parse.quote(f"site:linkedin.com {name_or_company}")}'
        ]
    }
    return dossier

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OSINT Investigator Skill Agnóstica')
    parser.add_argument('--target', required=True, help='Nombre del ejecutivo o empresa objetivo')
    parser.add_argument('--domain', help='Dominio web asociado')
    
    args = parser.parse_args()
    print(f"=== OSINT INVESTIGATOR SKILL: {args.target} ===")
    res = osint_dossier_search(args.target, args.domain)
    print(json.dumps(res, indent=2, ensure_ascii=False))
