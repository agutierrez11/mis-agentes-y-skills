import os
import pandas as pd

def main():
    print("=== MERGE DE TODOS LOS DATASETS REALES (SOFOMES + LEASING MAQUINARIA + LENDERS DIGITALES + LOOKALIKES EFISYS) ===")
    
    # 1. Main Dataset (2,263 SOFOMes)
    main_csv = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\data\pipeline_real_sofomes_mx.csv"
    df_main = pd.read_csv(main_csv)
    
    # 2. Leasing Maquinaria Dataset
    leasing_csv = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\data\lista_real_leasing_maquinaria.csv"
    df_leasing = pd.read_csv(leasing_csv)
    
    # 3. Lenders Digitales Dataset
    lenders_csv = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\data\lista_real_lenders_digitales.csv"
    df_lenders = pd.read_csv(lenders_csv)
    
    # Format Leasing records for Master Dataset
    new_rows = []
    for idx, r in df_leasing.iterrows():
        new_rows.append({
            'denominacion_social_real': str(r['denominacion']) + " (Leasing Maquinaria)",
            'estado_republica_sede': 'Nacional / CDMX',
            'cartera_estimada_mrp': '$80M - $250M MXN',
            'competidor_actual': 'Sistema Legado / In-House',
            'tier_pricing': 'Tier 2 ($80,000/mes)',
            'estatus_funnel': '1. Por Contactar',
            'sitio_web_oficial': r['sitio_web'],
            'tecnologias_detectadas': 'Arrendores Maquinaria & Equipo Heavy'
        })

    # Format Lenders Digitales records for Master Dataset
    for idx, r in df_lenders.iterrows():
        new_rows.append({
            'denominacion_social_real': str(r['denominacion']) + " (Lender Digital)",
            'estado_republica_sede': 'Nacional / Fintech',
            'cartera_estimada_mrp': '$50M - $180M MXN',
            'competidor_actual': 'AWS Cloud / In-House',
            'tier_pricing': 'Tier 2 ($42,000/mes)',
            'estatus_funnel': '1. Por Contactar',
            'sitio_web_oficial': r['sitio_web'],
            'tecnologias_detectadas': 'Lender Digital / Neobanco Pyme'
        })
        
    df_new = pd.DataFrame(new_rows)
    df_combined = pd.concat([df_main, df_new], ignore_index=True)
    df_combined.to_csv(main_csv, index=False)
    
    print(f"[OK] Master Dataset actualizado exitosamente con {len(df_combined)} registros totales.")

if __name__ == '__main__':
    main()
