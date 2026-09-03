import os, sys, argparse, json

def generate_sales_stage_script(company, stage, pain_point="mermas de efectivo y colas en isla"):
    """
    Motor de ventas contextual SalesGPT (https://github.com/filip-michalsky/SalesGPT).
    Modela el discurso del agente según la etapa de la conversación de ventas.
    """
    stages = {
        "1_prospeccion": {
            "Objetivo": "Captar atención en los primeros 5 segundos",
            "Guion_WhatsApp": f"Hola [Nombre], te escribo rápido porque estamos ayudando a directivos de estaciones como {company} a cortar los tiempos de cobro a 45 segundos. ¿Tienes 3 minutos hoy?",
            "Guion_Email_Asunto": f"Pregunta rápida sobre tiempos de carga en {company}"
        },
        "2_calificacion": {
            "Objetivo": "Validar si tienen dolor real y volumen suficiente",
            "Preguntas_Filtro": [
                "¿Cuántos vehículos despachan por isla en horas pico?",
                "¿El despachador cobra en efectivo o con terminal bancaria inalámbrica?",
                "¿Tienen mermas de corte al final de cada turno?"
            ]
        },
        "3_propuesta_valor": {
            "Objetivo": "Presentar el quiosco SmartPOS con riesgo cero",
            "Discurso": f"En PayMind instalamos un Quiosco SmartPOS piloto en tu estación principal por 14 días. Si no reduce el tiempo a la mitad y elimina las mermas de turno, lo retiramos sin costo alguno."
        },
        "4_manejo_objeciones": {
            "Objecion_Ya_Tengo_Terminales": "Nuestras soluciones no compiten con tus terminales de mano; son quioscos de autoservicio que liberan a tus despachadores para atender más bombas.",
            "Objecion_No_Quiero_Cambiar_Sistema": "PayMind no te pide cambiar tu software de control volumétrico (ControlGAS, Alvic, SIGMA); nos conectamos directo a tu operación actual."
        },
        "5_cierre": {
            "Objetivo": "Agendar fecha de instalación o demo en vivo",
            "Cierre_Alternativo": "¿Te queda mejor que programemos la visita técnica este jueves por la mañana o el viernes por la tarde?"
        }
    }
    
    stage_key = [k for k in stages.keys() if stage.lower() in k]
    selected_stage = stages[stage_key[0]] if stage_key else stages["1_prospeccion"]
    
    return {
        "Company": company,
        "Selected_Stage": stage,
        "Script_Data": selected_stage
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="SalesGPT Contextual Sales Agent")
    parser.add_argument("--company", required=True, help="Nombre de la empresa prospecto")
    parser.add_argument("--stage", default="prospeccion", choices=["prospeccion", "calificacion", "propuesta_valor", "manejo_objeciones", "cierre"], help="Etapa de la conversación de ventas")
    args = parser.parse_args()
    print(json.dumps(generate_sales_stage_script(args.company, args.stage), indent=2, ensure_ascii=False))
