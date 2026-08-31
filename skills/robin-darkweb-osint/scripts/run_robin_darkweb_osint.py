import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Runner para Robin Darkweb OSINT")
    parser.add_argument("--target", help="Dominio o palabra clave a investigar", default="sample")
    parser.add_argument("--depth", help="Nivel de profundidad OSINT", type=int, default=2)
    args, unknown = parser.parse_known_args()
    
    print(f"=== EJECUTANDO SKILL: robin-darkweb-osint ===")
    print(f"Objetivo OSINT: {args.target}")
    print(f"Profundidad: {args.depth}")
    print(f"Repo Origen: https://github.com/apurvsinghgautam/robin")
    print(f"Estado: Investigación OSINT simulada completada con éxito.")

if __name__ == "__main__":
    main()
