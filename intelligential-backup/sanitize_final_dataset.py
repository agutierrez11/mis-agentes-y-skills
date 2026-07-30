import pandas as pd
import re

csv_path = "c:/Users/Antonio/.gemini/antigravity-ide/scratch/intelligential/data/pipeline_real_sofomes_mx.csv"
df = pd.read_csv(csv_path)

print(f"Initial count: {len(df)}")

# Filter rules for valid company names
def is_valid_company_name(name):
    s = str(name).strip()
    if len(s) < 5 or len(s) > 110:
        return False
    if any(ext in s.lower() for ext in ['.png', '.jpg', '.jpeg', '.svg', '.gif', 'asofom.mx', 'http', 'www', 'comite', 'comité', 'encuentro', 'convencion', 'regional']):
        return False
    # Must contain corporate markers
    corporate_markers = ['SOFOM', 'S.A.', 'S.A.P.I.', 'ARRENDADORA', 'FINANCIERA', 'LEASING', 'CAPITAL', 'FACTORAJE', 'CREDITO', 'FINANCIERO']
    return any(marker in s.upper() for marker in corporate_markers)

clean_df = df[df['denominacion_social_real'].apply(is_valid_company_name)].copy()

# Re-index
clean_df['id'] = range(1, len(clean_df) + 1)
clean_df.to_csv(csv_path, index=False, encoding='utf-8-sig')

print(f"Cleaned final count: {len(clean_df)}")
