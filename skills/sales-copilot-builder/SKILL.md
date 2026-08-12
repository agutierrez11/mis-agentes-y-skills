---
name: sales-copilot-builder
description: >
  Construye Copilotos de Ventas B2B agnósticos: motor de objeciones CPS (Customer Problem Selling),
  calculadora de CDI (Costo Diario de Ineficiencia), perfilamiento DISC local sin API de pago,
  y outbound relevance matrix. Funciona en Streamlit, HTML estático o FastAPI.
  Úsalo en cualquier proyecto de ventas enterprise, no solo en pagos.
---

# Sales Copilot Builder — Framework Agnóstico de Copiloto de Ventas B2B

## Cuándo usar esta Skill

- Construir un copiloto de ventas para **cualquier industria** (pagos, SaaS, fintech, ERP, etc.)
- Agregar motor de objeciones CPS en tiempo real a un proyecto
- Calcular el Costo Diario de Ineficiencia (CDI) del prospecto para crear urgencia
- Adaptar el pitch automáticamente al perfil DISC del decisor

---

## 🧠 Los 4 Módulos del Sales Copilot Framework

### 1. Motor de Objeciones CPS (Customer Problem Selling)

**Principio:** Toda objeción es un problema no articulado. El copiloto convierte la objeción en una pregunta socrática que revela el costo del statu quo.

```python
CPS_OBJECTIONS = {
    "Es muy caro": {
        "reframe": "¿Cuánto le cuesta hoy el problema que esto resuelve?",
        "socratic": "Si el costo de NO resolver esto es mayor que la renta mensual, ¿qué es más caro?",
        "cdi_trigger": True  # Activa calculadora CDI
    },
    "Ya tenemos un proveedor": {
        "reframe": "¿Cuándo fue la última vez que ese proveedor los ayudó a crecer?",
        "socratic": "¿Qué capacidad les falta hoy que ese proveedor no puede darles?",
        "cdi_trigger": False
    },
    "No es el momento": {
        "reframe": "¿Qué tendría que pasar para que sea el momento correcto?",
        "socratic": "Cada mes que esperan es otro mes de [pérdida cuantificada]. ¿Cuándo comienza a ser urgente?",
        "cdi_trigger": True
    }
}
```

### 2. Calculadora CDI (Costo Diario de Ineficiencia)

**Fórmula:**
```
CDI = (horas_perdidas_dia × costo_hora) + (riesgo_multa / 365) + (perdida_clientes_mes × ticket_promedio / 30)
```

```python
def calcular_cdi(horas_excel=6, costo_hora=250, riesgo_multa=500_000,
                 clientes_perdidos=2, ticket_promedio=5_000):
    cdi = (horas_excel * costo_hora) + (riesgo_multa / 365) + (clientes_perdidos * ticket_promedio / 30)
    return round(cdi, 2)

# Ejemplo: CDI = $7,419 MXN/día → "Cada día que esperan les cuesta $7,419"
```

**Integración en pitch:**
> *"Basado en los números que me dio, el Costo Diario de Ineficiencia de su operación actual es de $[CDI] pesos. Cada día que no resuelven esto, ese dinero sale de su EBITDA."*

### 3. Perfilamiento DISC Local (Sin Pagar API)

```python
def predict_disc(job_title="", country="", text_bio=""):
    title = job_title.lower()
    
    # D — Dominante (C-Level, Ventas, Asia)
    if any(k in title for k in ["ceo", "cfo", "vp", "head", "director", "founder"]) or "asia" in country.lower():
        return {"type": "D", "rule": "45-60s, numeración oral, datos duros, cero small talk"}
    
    # C — Concienzudo (Tech, Engineering, Compliance)
    elif any(k in title for k in ["cto", "tech", "architect", "engineer", "compliance", "legal"]):
        return {"type": "C", "rule": "Métricas exactas, arquitectura de solución, SLAs, documentación"}
    
    # S — Sólido (HR, Operations, Customer Success)
    elif any(k in title for k in ["ops", "operations", "hr", "success", "recruiter", "talent"]):
        return {"type": "S", "rule": "Foco en adopción, cero fricciones, soporte garantizado"}
    
    # I — Influyente (Marketing, Growth, BD)
    return {"type": "I", "rule": "Visión, escala, casos de éxito, co-selling opportunities"}
```

### 4. Outbound Relevance Matrix (Atractores Cognitivos)

**Principio:** El primer mensaje debe inyectar una anomalía cognitiva que rompa el statu quo en 3 segundos.

| Perfil Decisor | Ansiedad Principal | Atractor Cognitivo |
|---------------|-------------------|-------------------|
| CEO/Founder | Escala / Quemarse | *"Su competidor abrió 3 mercados nuevos sin contratar"* |
| CFO | EBITDA / Multas | *"Están perdiendo $X/día sin saberlo"* |
| CTO | Deuda técnica | *"Su integración actual tiene 4 puntos de falla regulatoria"* |
| Head of Sales | Cuota / Pipeline | *"Sus vendedores pierden 6h/semana en tareas que IA puede hacer"* |

---

## 🖥️ Implementación en Streamlit (Plantilla Base)

```python
import streamlit as st

st.set_page_config(page_title="Sales Copilot", page_icon="⚡", layout="wide")

tab_objections, tab_outbound, tab_cdi = st.tabs([
    "💡 Motor de Objeciones", "🎯 Outbound Matrix", "📊 CDI Calculator"
])

with tab_objections:
    objection = st.selectbox("Objeción detectada:", list(CPS_OBJECTIONS.keys()))
    if st.button("⚡ Generar Respuesta CPS"):
        data = CPS_OBJECTIONS[objection]
        st.success(f"🔄 **Reframe:** {data['reframe']}")
        st.info(f"🧠 **Socrática:** {data['socratic']}")

with tab_cdi:
    horas = st.slider("Horas perdidas en Excel/día", 1, 12, 6)
    costo = st.number_input("Costo laboral/hora (MXN)", value=250)
    cdi = calcular_cdi(horas_excel=horas, costo_hora=costo)
    st.metric("💸 Costo Diario de Ineficiencia", f"${cdi:,.2f} MXN/día")
```

---

## 📦 Archivos del Framework

| Archivo | Propósito |
|---------|-----------|
| `app_copilot_cps.py` | App Streamlit principal |
| `crystal_knows_integration.py` | DISC profiler local |
| `cps_database.py` | Base de datos de objeciones y respuestas |
| `game_theory_engine.py` | Módulo de teoría de juegos para negociación |
| `copilot.html` | PWA de copiloto con audio en tiempo real |

---

## 🚀 Instrucciones de Despliegue

```bash
# Local (desarrollo)
python -m streamlit run app_copilot_cps.py --server.port 8501

# GitHub Pages (frontend estático)
# → El copilot.html usa Web Speech API, funciona sin backend

# Producción con backend
python app_copilot_server.py  # FastAPI + SSE para streaming de audio
```
