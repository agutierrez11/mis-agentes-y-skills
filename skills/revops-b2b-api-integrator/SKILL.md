---
name: revops-b2b-api-integrator
description: Selección, integración y arquitectura de APIs de prospección B2B, enriquecimiento de datos de leads, servidores MCP y conectores de RevOps para CPS Platform y Radar Comercial inspirado en cporter202 (agentic-ai-apis).
---

# Skill: RevOps & B2B API Integrator

## Propósito
Guiar la selección e integración de APIs de producción preparadas para agentes de IA (Agentic APIs / MCP Servers), enfocadas en enriquecimiento de prospectos, scraping ético, validación de datos comerciales y automatización de pipelines de ventas B2B.

## Casos de Uso & Arquitectura
1. **Enriquecimiento de Leads & ICP Matching:**
   - Integración de conectores para extracción de datos de dominios, cargos directivos, tecnologías utilizadas (Tech stack lookups) y tamaño de empresa.
2. **Servidores MCP para Agentes Comerciales:**
   - Protocolo Model Context Protocol (MCP) para conectar el copiloto de ventas con CRMs (HubSpot, Salesforce, CompAI CRM) y motores de prospección.
3. **Scraping Ético & Normalización:**
   - Extracción estructurada en JSON/Markdown de páginas corporativas, normalizando acentos y nombres para evitar falsos negativos en filtros comerciales.

## Best Practices
- Mantener siempre fallbacks y manejo elegante de cuotas de APIs externas.
- Garantizar que los leads enriquecidos cumplan con el esquema unificado de CPS Platform.
