import argparse, json

def design_agent_loop(goal_description, interval_minutes=60):
    """
    Diseñador agnóstico de bucles autónomos (https://github.com/groktopus/loop-designer)
    """
    steps = [
        "1. Definición clara del objetivo (/goal)",
        "2. Identificación del estado inicial e inputs",
        "3. Criterio de verificación de éxito (Definition of Done)",
        "4. Definición de frecuencia / cron schedule",
        "5. Mecanismo de persistencia de memoria (DB/JSON/MD)",
        "6. Manejo autónomo de excepciones y reintentos",
        "7. Salvaguardas anti-loop infinito (Max iterations limit)",
        "8. Notificaciones de avance sintetizadas",
        "9. Protocolo de fallback en caso de error crítico",
        "10. Registro de auditoría y traza de trajín (Transcript)"
    ]
    return {
        "Goal": goal_description,
        "Interval_Minutes": interval_minutes,
        "Architecture_Steps": steps,
        "Status": "Loop_Designed_Successfully"
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--goal", required=True)
    parser.add_argument("--interval", type=int, default=60)
    args = parser.parse_args()
    print(json.dumps(design_agent_loop(args.goal, args.interval), indent=2, ensure_ascii=False))
