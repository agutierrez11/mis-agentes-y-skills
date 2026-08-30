---
name: openexecutive-csuite-agent
description: Operación, arquitectura e integración de OpenExecutive (SenteLabsAI/OpenExecutive), el sistema agéntico de C-Suite virtual con 8 agentes especializados (CSO, CFO, CMO, CTO, etc.) para toma de decisiones gerenciales B2B.
---

# 🏛️ OpenExecutive C-Suite Agent Skill

Esta skill define la arquitectura, integración y operación de **OpenExecutive** (`SenteLabsAI/OpenExecutive`), una plataforma agéntica que simula un equipo ejecutivo completo C-Suite respaldado por modelos de lenguaje avanzados (Claude / Gemini).

---

## 🎯 Propósito y Casos de Uso

1. **Simulación Ejecutiva C-Suite:** Proveer una voz ejecutiva coherente y especializada para startups y empresas B2B.
2. **Evaluación Estratégica de Negocios:** Análisis de fusiones y adquisiciones (M&A), unit economics, posicionamiento competitivo y estrategia de go-to-market.
3. **Definición y Seguimiento de OKRs:** Traducir objetivos comerciales de alto nivel en métricas ejecutables para células agénticas y equipos de desarrollo.

---

## 🤖 Los 8 Agentes Especializados de C-Suite

| Rol Ejecutivos | Dominio de Responsabilidad | Prompting & Modelo de Enfoque |
| :--- | :--- | :--- |
| **CSO (Chief Strategy Officer)** | Análisis competitivo, matriz de mercado, alianzas y M&A. | Enfoque MEDDIC / Mckinsey 7S. |
| **CFO (Chief Financial Officer)** | Modelado financiero, proyecciones de burn rate, LTV/CAC, unit economics. | Métricas SaaS / RevOps. |
| **CMO (Chief Marketing Officer)** | Estrategias de posicionamiento, embudo Inbound/Outbound, branding. | Copywriting B2B & Growth Loops. |
| **CTO (Chief Technology Officer)** | Arquitectura de software, evaluación de stack, deuda técnica, CI/CD. | Clean Architecture, Scalability. |
| **CPO (Chief Product Officer)** | Definición de backlog, ROI por feature, estrategia UX/UI. | Product-Led Growth (PLG). |
| **CRO (Chief Revenue Officer)** | Pipeline de ventas, incentivos de co-selling, conversión de leads. | RevOps & Speed to Sell. |
| **CLO (Chief Legal Officer)** | Privacidad de datos (GDPR, Zero-Knowledge), compliance, contratos. | Risk Mitigation & IP Protection. |
| **COO (Chief Operating Officer)** | Eficiencia operativa, automatización de workflows agénticos, SLA. | Process Optimization. |

---

## ⚙️ Stack Técnico e Integración

* **Frontend:** Next.js (TypeScript) con interfaz estilo dashboard ejecutivo.
* **Backend:** API en FastAPI (Python) con arquitectura asíncrona.
* **Motor LLM:** Anthropic Claude (Claude Opus 3.7 / Claude Sonnet) o Google Gemini (Gemini 2.5 Flash / 3.1 Pro) con extended thinking.

---

## 🔄 Flujo de Integración con Radar Comercial

1. **Feedback de Pipeline:** El **CRO Agent** analiza la densidad de contactos de 1er grado extraídos de LinkedIn y ajusta el *bounty* ($150 USD) y comisiones de co-selling.
2. **Priorización de Cuentas Objetivo:** El **CSO Agent** evalúa los sectores de mayor conversión para enfocar el enriquecimiento incremental (HarvestAPI/Apify).
3. **Soberanía y Compliance:** El **CLO Agent** garantiza que el modelo BYOD (Bring Your Own Data) cumpla con Zero-Knowledge en IndexedDB.
