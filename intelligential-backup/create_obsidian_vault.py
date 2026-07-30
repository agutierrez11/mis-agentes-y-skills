import os
import json

base = r'c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential\obsidian_vault'
dirs = [
    '01-Objeciones',
    '02-Competidores',
    '03-WinAnalysis',
    '04-Ecosistema_Aliados',
    '05-Playbooks',
    '.obsidian'
]

for d in dirs:
    os.makedirs(os.path.join(base, d), exist_ok=True)

# 1. Config obsidian app.json
app_config = {
    "useMarkdownLinks": True,
    "livePreview": True,
    "attachmentFolderPath": "/"
}

with open(os.path.join(base, '.obsidian', 'app.json'), 'w', encoding='utf-8') as f:
    json.dump(app_config, f, indent=2)

# 2. Objeción Contrato Vigente
with open(os.path.join(base, '01-Objeciones', 'Objecion_Contrato_Vigente.md'), 'w', encoding='utf-8') as f:
    f.write("""# 🛡️ Objeción: 'Tengo contrato vigente con otro proveedor (DynamiCore)'

## 🎯 Diagnóstico MEDDIC
- **Freno principal:** Miedo a pagar doble renta durante la migración.
- **Enlace a Competidor:** [[Battlecard_DynamiCore]]

## ⚔️ Respuesta Comercial (Oferta Migración Sin Doble Costo)
> "Si te faltan de 3 a 6 meses de contrato con tu proveedor actual, Intelligential te bonifica el 100% de la renta mensual durante esos meses. Solo pagas tu Setup Fee (2x renta) y dejamos tu sistema [[4_Pilares_del_Credito]] listo en 30 días."

## 🔗 Notas Relacionadas
- [[Playbook_MEDDIC_Discovery]]
- [[Scripts_ReEngagement]]
""")

# 3. Objeción Presupuesto / Setup Fee
with open(os.path.join(base, '01-Objeciones', 'Objecion_Presupuesto_Setup.md'), 'w', encoding='utf-8') as f:
    f.write("""# 💰 Objeción: 'El Setup Fee o Renta nos parece cara'

## 🎯 Diagnóstico MEDDIC
- **Freno principal:** El cliente compara únicamente la renta base ($50k vs $30k) sin ver los parches externos.
- **Respuesta en TCO:** Demostrar el ahorro de > 42% anual.

## ⚔️ Respuesta Comercial
> "La renta base de DynamiCore no incluye el módulo PLD ($12k/mes), ni los conectores API de Buró/Mifiel ($80k en desarrollo). En Intelligential el Plan Smarty incluye todo sin sorpresas por $50k/mes y Setup de 2x renta."

## 🔗 Notas Relacionadas
- [[Battlecard_DynamiCore]]
- [[4_Pilares_del_Credito]]
""")

# 4. Battlecard DynamiCore
with open(os.path.join(base, '02-Competidores', 'Battlecard_DynamiCore.md'), 'w', encoding='utf-8') as f:
    f.write("""# ⚔️ Battlecard: Intelligential vs. DynamiCore

## 📊 Comparativa TCO (Año 1)
- **Intelligential:** $700,000 MXN (Setup 2x Renta + $50k/mes todo incluido)
- **DynamiCore:** $1,220,000+ MXN (Cobros separados por PLD, conectores y parches)
- **Ahorro Neto:** > 42% de ahorro real ($520k MXN).

## 🎯 Contra-Golpes de Ventas
1. **Salida a Producción:** Intelligential en 30 días vs. 8 meses de DynamiCore.
2. **PLD Nativo:** Cumplimiento CNBV en el core desde el día 1.
3. **Ecosistema:** Pre-integrado con [[Mifiel_STP_Nubarium]].

## 🔗 Notas Relacionadas
- [[Objecion_Contrato_Vigente]]
- [[Casos_de_Exito_SOFOM]]
""")

# 5. Ecosistema Aliados
with open(os.path.join(base, '04-Ecosistema_Aliados', 'Mifiel_STP_Nubarium.md'), 'w', encoding='utf-8') as f:
    f.write("""# 🤝 Ecosistema de Aliados Pre-Integrados

Intelligential conecta nativamente con los líderes del mercado sin costo extra por conector:

- **Firma Electrónica:** Mifiel, Weetrust
- **Dispersión & SPEI:** STP, Monato
- **KYC & Identidad:** Nubarium (INE / SAT)
- **Scores & Data:** Syntage, Nufi, Moffin

## 🔗 Notas Relacionadas
- [[Battlecard_DynamiCore]]
- [[4_Pilares_del_Credito]]
""")

# 6. 4 Pilares del Credito
with open(os.path.join(base, '4_Pilares_del_Credito.md'), 'w', encoding='utf-8') as f:
    f.write("""# 🏛️ Los 4 Pilares del Crédito (Smart Native®)

1. **Pilar 01: Core Financiero** — Administración de cartera y reportes.
2. **Pilar 02: Solicitud Digital** — Originación 100% sin papel.
3. **Pilar 03: Onboarding & KYC** — Validación INE y SAT nativa.
4. **Pilar 04: Cumplimiento PLD/FT** — Regulación CNBV desde el Día 1.

## 🔗 Notas Relacionadas
- [[Battlecard_DynamiCore]]
- [[Mifiel_STP_Nubarium]]
""")

# 7. Playbook MEDDIC Discovery
with open(os.path.join(base, '05-Playbooks', 'Playbook_MEDDIC_Discovery.md'), 'w', encoding='utf-8') as f:
    f.write("""# 📋 Playbook MEDDIC: Preguntas de Descubrimiento

1. **Metrics:** ¿Cuánto tiempo tarda hoy tu equipo en originar un crédito desde la solicitud hasta la dispersión con SPEI?
2. **Economic Buyer:** ¿Quién aprueba el presupuesto del Setup Fee (2x renta) en el consejo?
3. **Decision Criteria:** ¿Cuáles son los 3 requerimientos indispensables de tu Oficial de Cumplimiento PLD?
4. **Decision Process:** ¿Qué fecha límite tienen para salir a producción?
5. **Identify Pain:** ¿Qué problemas les genera tener el Core separado del sistema de PLD o Buró?

## 🔗 Notas Relacionadas
- [[Objecion_Contrato_Vigente]]
- [[Battlecard_DynamiCore]]
""")

print("[OK] Boveda fisica de Obsidian creada exitosamente en:", base)
