import os, sys, argparse, json

BLUEPRINTS = {
    "b2b_outbound_pipeline": {
        "Nombre": "Pipeline Multi-Agente de Prospección B2B",
        "Descripcion": "Flujo desatendido de 4 agentes especializados para calificar y contactar cuentas enterprise.",
        "Agentes_Involucrados": [
            {"Rol": "Scout Agent", "Herramienta": "Crawl4AI", "Tarea": "Rastrear sitio institucional, dominio y directorios regulatorios."},
            {"Rol": "Forensic Profiler", "Herramienta": "OSINT Investigator", "Tarea": "Detectar stack técnico (core bancario, rieles STP, ERP) y regulaciones que le aprietan."},
            {"Rol": "Decision Hunter", "Herramienta": "LinkedIn Dorker", "Tarea": "Extraer nombre y perfil del CFO, Director de Cobranza o Head of Payments."},
            {"Rol": "Copy Architect", "Herramienta": "SalesGPT (PAS Framework)", "Tarea": "Redactar mensaje quirúrgico de 3 párrafos directo al dolor técnico detectado."}
        ],
        "Entregable": "Ficha de contacto con borrador de mensaje listo para disparar y agenda de reunión remota."
    },
    "deep_research_dossier": {
        "Nombre": "Fábrica de Investigación Profunda de Entidades",
        "Descripcion": "Generador automatizado de fichas técnicas para reuniones C-Level.",
        "Agentes_Involucrados": [
            {"Rol": "Financial Rating Reader", "Tarea": "Extraer reportes de calificadoras (Fitch, HR Ratings, Moody's)."},
            {"Rol": "Regulatory Auditor", "Tarea": "Consultar circulares de Banxico, Buró de Entidades Financieras y SIPRES."},
            {"Rol": "Executive Summarizer", "Tarea": "Condensar los dolores en un pitch de 60 segundos."}
        ],
        "Entregable": "Dossier ejecutivo de 1 página con ganchos de conversación para el vendedor."
    },
    "autonomous_followup_loop": {
        "Nombre": "Ciclo de Seguimiento Asistido sin Fricción",
        "Descripcion": "Secuencia de 3 contactos multicanal para cuentas que no contestaron el primer mensaje.",
        "Agentes_Involucrados": [
            {"Rol": "Day 3 Bump", "Canal": "LinkedIn", "Enfoque": "Compartir un benchmark o caso de éxito del sector."},
            {"Rol": "Day 7 Technical Insight", "Canal": "Email", "Enfoque": "Mencionar impacto en reducción de costos de transacción."},
            {"Rol": "Day 12 Breakup Note", "Canal": "Email", "Enfoque": "Cierre cortés liberando la agenda del decisor."}
        ],
        "Entregable": "Cadena de seguimiento programable en CRM o envío manual."
    }
}

def get_blueprint(blueprint_type=None):
    if blueprint_type and blueprint_type in BLUEPRINTS:
        return BLUEPRINTS[blueprint_type]
    return {
        "Fuente_Oficial": "https://github.com/hesamsheikh/awesome-openclaw-usecases",
        "Total_Blueprints_Disponibles": len(BLUEPRINTS),
        "Blueprints": BLUEPRINTS
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="OpenClaw Agent Orchestration Blueprints Engine")
    parser.add_argument("--type", choices=["b2b_outbound_pipeline", "deep_research_dossier", "autonomous_followup_loop"], help="Tipo de blueprint a consultar")
    args = parser.parse_args()
    print(json.dumps(get_blueprint(args.type), indent=2, ensure_ascii=False))
