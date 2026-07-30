# ==============================================================================
# GENERADOR DE MENSAJES OUTBOUND CPS (RELEVANCE FIRST / INYECCIÓN DE ANOMALÍA)
# ==============================================================================
import json

CPS_MESSAGING_MATRIX = {
    "CEO": {
        "attractor": "Ansiedad por Escala & Eficiencia Marginal",
        "linkedin_hook": "Veo que están expandiendo su colocación en México. Tradicionalmente, duplicar la cartera implica duplicar la nómina operativa por parches en Excel. ¿Cómo están resolviendo la escalabilidad marginal de su Core?",
        "phone_trigger": "No te llamo para venderte un software. Te llamo porque el Costo Diario de la Ineficiencia (CDI) de una SOFOM de tu tamaño suele ser de $15,000 pesos por culpa de la fragmentación de proveedores. ¿Tienes 3 minutos para evaluar tu métrica?"
    },
    "COMPLIANCE": {
        "attractor": "Pánico a Multas CNBV & Retrabajo PLD",
        "linkedin_hook": "Con las nuevas auditorías de la CNBV, el retrabajo manual de PLD está costando días de estrés. ¿Tu sistema actual genera el reporte en un clic o tu equipo pasa el fin de semana cruzando datos?",
        "phone_trigger": "Monitoreamos las multas de la CNBV en el sector. Las financieras están perdiendo licencias por falta de automatización nativa en su onboarding. ¿Cómo mitigan ese riesgo de transición hoy?"
    },
    "IT_DIRECTOR": {
        "attractor": "Autoprotección de Código & Backlog Saturado",
        "linkedin_hook": "Ingeniero, la mayoría de las SOFOMes obligan a TI a pasar el 80% del tiempo parchando APIs reguladas en lugar de programar sus algoritmos de scoring. ¿Cómo proteges tu backlog?",
        "phone_trigger": "Ingeniero, directo al grano: sé que tu equipo prefiere desarrollar código propietario que estar pegando APIs de KYC y Firma de proveedores externos. ¿Qué tan atrapado está tu pipeline técnico actual?"
    }
}

def generate_cps_outbound_message(role, channel, institution_name, cdi_projected_mxn=15000):
    """Genera un mensaje outbound basado en la Inyección de Anomalía de CPS"""
    role_data = CPS_MESSAGING_MATRIX.get(role, CPS_MESSAGING_MATRIX["CEO"])
    
    if channel == "LinkedIn":
        hook = role_data["linkedin_hook"]
        return f"Hola, {institution_name}. {hook}"
    else:
        trigger = role_data["phone_trigger"]
        return f"[Trigger Telefónico 15 Segundos]: {trigger}"

if __name__ == "__main__":
    print("=== MUESTRA DE GENERACIÓN OUTBOUND CPS ===")
    print(generate_cps_outbound_message("CEO", "LinkedIn", "MexCredit SOFOM"))
    print(generate_cps_outbound_message("COMPLIANCE", "Phone", "Financiera Bajío"))
