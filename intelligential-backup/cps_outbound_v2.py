# ==============================================================================
# GENERADOR DE MENSAJES OUTBOUND CPS V2 (RELEVANCE FIRST / INYECCIÓN DE ANOMALÍA)
# ==============================================================================
import json
import os

# ==============================================================================
# GENERADOR DE MENSAJES OUTBOUND CPS V2 (RELEVANCE FIRST + MÉTODO SOCRÁTICO)
# Basado en Cuadernos de NotebookLM: "Método Socrático de Ventas" & "CPS Coach"
# ==============================================================================
import json
import os

CPS_MESSAGING_MATRIX = {
    "CEO": {
        "attractor": "Ansiedad por Escala & Eficiencia Marginal",
        "pain": "Duplicar cartera implica duplicar la nómina operativa por parches en Excel y fragmentación de software.",
        "linkedin_hook": "Hola {name}, vi que en {institution} están expandiendo colocación. Pregunta rápida: si tuvieran una varita mágica para duplicar cartera sin contratar más personal operativo, ¿qué cuello de botella tendrían que resolver hoy?",
        "phone_trigger": "Hola {name}, no te llamo para venderte nada. Te llamo porque calculamos un Costo Diario de Ineficiencia (CDI) en {institution} de ${cdi:,.2f} MXN/día. ¿Qué pasaría si ese costo sigue corriendo hasta fin de año?",
        "email_subject": "Pregunta de escala en {institution} vs. Costo Diario de Ineficiencia (${cdi:,.2f}/día)",
        "socratic_question": "¿En una escala del 1 al 10, qué tan tranquilos están con la velocidad de originación de sus créditos actuales?"
    },
    "CFO": {
        "attractor": "Fuga de Margen & Costo Diario de Ineficiencia (CDI)",
        "pain": "Costo de capital elevado y falta de retorno en licencias de software no utilizadas.",
        "linkedin_hook": "Hola {name}, calculamos que el Costo Diario de Ineficiencia en {institution} asciende a ${cdi:,.2f} MXN/día. ¿Cuánto les cuesta a fin de mes la demora de 3 días en autorizar un crédito?",
        "phone_trigger": "Hola {name}, directo al grano: ¿cuándo fue la última vez que auditaron el costo oculto de mantener 4 licencias sueltas de software en lugar de una plataforma unificada?",
        "email_subject": "Implicación financiera: CDI de ${cdi:,.2f} MXN/día en {institution}",
        "socratic_question": "¿Si demostramos que el TCO baja 42% en el Año 1, valdría la pena revisar el contrato vigente?"
    },
    "COMPLIANCE": {
        "attractor": "Pánico a Multas CNBV & Retrabajo PLD",
        "pain": "Listas bloqueadas y matrices de riesgo procesadas manualmente en hojas de cálculo.",
        "linkedin_hook": "Hola {name}, con las auditorías SITI PLD 2026 de la CNBV, ¿cuánto tiempo le toma a tu equipo generar la evidencia del informe mensual? ¿Es en 1 clic o cruzan datos a mano?",
        "phone_trigger": "Hola {name}, vimos las sanciones recientes de CNBV en el sector SOFOM. ¿Qué pasaría si la CNBV les audita un expediente procesado manualmente este mes?",
        "email_subject": "Pregunta de auditoría CNBV / PLD en {institution}",
        "socratic_question": "¿Qué tan preparados están para responder a un requerimiento de la CNBV en menos de 24 horas?"
    },
    "IT_DIRECTOR": {
        "attractor": "Autoprotección de Código & Backlog Saturado",
        "pain": "Pasar el 80% del tiempo pegando APIs reguladas y resolviendo incidencias en lugar de crear valor.",
        "linkedin_hook": "Hola {name}, habitualmente los CTOs pasan el 80% del tiempo manteniendo APIs de KYC/Firma externa en lugar de programar scoring propio. ¿Qué pasaría si liberaran a tu equipo de esa carga?",
        "phone_trigger": "Ingeniero, directo al punto: si tuvieras que elegir entre mantener parches de software viejo o desplegar en 30 días con APIs nativas, ¿cuál preferirías?",
        "email_subject": "Liberación de backlog técnico en {institution}",
        "socratic_question": "¿Cuántas horas al mes invierte tu equipo reparando conectores de proveedores externos?"
    }
}

def calculate_cdi(portfolio_size_mxn=100000000, manual_hours_per_month=120):
    """Calcula el Costo Diario de la Ineficiencia (CDI)"""
    daily_cost = (manual_hours_per_month * 450.0) / 30.0 + (portfolio_size_mxn * 0.0001)
    return round(daily_cost, 2)

def generate_cps_outbound_v2(role, channel, institution_name, contact_name="Director", portfolio_mxn=100000000):
    """Genera mensaje outbound v2 completo"""
    cdi_val = calculate_cdi(portfolio_mxn)
    role_info = CPS_MESSAGING_MATRIX.get(role.upper(), CPS_MESSAGING_MATRIX["CEO"])
    
    if channel.lower() == "linkedin":
        msg = role_info["linkedin_hook"].format(name=contact_name, institution=institution_name, cdi=cdi_val)
    elif channel.lower() == "email":
        subj = role_info["email_subject"].format(institution=institution_name, cdi=cdi_val)
        body = role_info["linkedin_hook"].format(name=contact_name, institution=institution_name, cdi=cdi_val)
        msg = f"Asunto: {subj}\n\n{body}"
    else:
        msg = role_info["phone_trigger"].format(name=contact_name, institution=institution_name, cdi=cdi_val)
        
    return {
        "institution": institution_name,
        "role": role,
        "channel": channel,
        "cdi_projected": cdi_val,
        "attractor": role_info["attractor"],
        "message": msg
    }

if __name__ == "__main__":
    print("=== TEST GENERADOR OUTBOUND CPS V2 ===")
    res = generate_cps_outbound_v2("CEO", "LinkedIn", "MexCredit SOFOM", "Luis")
    print(json.dumps(res, indent=2, ensure_ascii=False))
