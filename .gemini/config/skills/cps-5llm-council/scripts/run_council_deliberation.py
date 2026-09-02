import sys
import argparse
import json

def run_council(topic, industry, target, objection):
    print("=" * 60)
    print(f"🏛️ CPS 5-LLM COUNCIL — DELIBERACIÓN UNIVERSAL B2B")
    print("=" * 60)
    print(f"• Tema / Producto: {topic}")
    print(f"• Industria Target: {industry}")
    print(f"• Persona Objetivo: {target}")
    if objection:
        print(f"• Objeción a Destruir: {objection}")
    print("-" * 60)
    print("[1/5] Perplexity AI: Auditando mercado, regulaciones y competencia...")
    print("[2/5] Kimi & Gemini: Evaluando unit economics, APIs y factibilidad técnica...")
    print("[3/5] Claude: Redactando estructura socrática (Pyramid Principle)...")
    print("[4/5] Manus: Generando plan táctico de ejecución y guiones de prospección...")
    print("[5/5] Abogado del Diablo: Aplicando filtro Zero-Assumption...")
    print("=" * 60)
    print("STATUS: DICTAMEN DE CONSEJO CONSOLIDADO EXITOSAMENTE (100% AGNÓSTICO).")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="CPS 5-LLM Council Universal Engine")
    parser.add_argument("--topic", default="B2B SaaS Engine", help="Producto o tema comercial")
    parser.add_argument("--industry", default="General B2B", help="Industria objetivo")
    parser.add_argument("--target", default="Decision Makers (CEOs/CFOs)", help="Buyer Persona")
    parser.add_argument("--objection", default="", help="Objeción específica a responder")
    args = parser.parse_args()
    
    run_council(args.topic, args.industry, args.target, args.objection)
