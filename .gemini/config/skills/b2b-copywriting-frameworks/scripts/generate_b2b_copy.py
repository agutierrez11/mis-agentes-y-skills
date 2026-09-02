import os
import sys
import argparse

def generate_b2b_pitch(product_name, target_persona, pain_point, solution):
    """
    Generador de Copywriting B2B basado en los frameworks de Corey Haines (Marketingskills).
    """
    pitch = {
        'Framework_PAS': {
            'Problema': f"¿Los dueños de {target_persona} siguen sufriendo por {pain_point}?",
            'Agitación': f"Esto causa mermas de dinero en cada turno y pérdida de control operacional.",
            'Solución': f"{product_name} resuelve este problema implementando {solution} con cero fricción."
        },
        'Framework_Cold_Email': {
            'Asunto': f"Consulta sobre {pain_point} en {target_persona}",
            'Cuerpo': f"Hola [Nombre],\n\nTe contacto porque ayudamos a {target_persona} a eliminar {pain_point} mediante {solution}.\n\n¿Tienes 10 minutos este jueves para mostrarte una prueba piloto de 14 días sin costo?\n\nSaludos,\n[Firma]"
        }
    }
    return pitch

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='B2B Copywriting Frameworks Skill')
    parser.add_argument('--product', required=True, help='Nombre del producto/servicio')
    parser.add_argument('--persona', required=True, help='Perfil de cliente objetivo')
    parser.add_argument('--pain', required=True, help='Dolor principal del cliente')
    parser.add_argument('--solution', required=True, help='Propuesta de solución')
    
    args = parser.parse_args()
    print(f"=== B2B COPYWRITING FRAMEWORKS: {args.product} para {args.persona} ===")
    res = generate_b2b_pitch(args.product, args.persona, args.pain, args.solution)
    
    print("\n--- FRAMEWORK PAS (Problem-Agitate-Solve) ---")
    for k, v in res['Framework_PAS'].items():
        print(f"{k}: {v}")
        
    print("\n--- GUION DE EMAIL FRÍO ---")
    print(f"Asunto: {res['Framework_Cold_Email']['Asunto']}\n")
    print(res['Framework_Cold_Email']['Cuerpo'])
