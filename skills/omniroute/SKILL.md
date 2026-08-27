---
name: omniroute
description: Configuración y uso de OmniRoute, el gateway de IA open-source para unificar +340 proveedores de IA con auto-fallback de cuotas y compresión de tokens RTK.
---

# OmniRoute: Gateway de IA Multiproyecto

## Descripción
OmniRoute (`diegosouzapw/OmniRoute`) es un gateway de IA open-source que unifica el acceso a más de 340 proveedores y 1,200 modelos en un único endpoint local o en la nube.

## Capacidades Principales
1. **Auto-Fallback Inteligente:** Si Groq, OpenAI o Gemini agotan su cuota (Rate Limit 429), OmniRoute redirige automáticamente la petición al siguiente mejor modelo disponible en milisegundos.
2. **Compresión de Tokens RTK:** Reduce entre 15% y 95% el consumo de tokens.
3. **Agregación de Camadas Gratuitas:** Gestiona más de 1.5 mil millones de tokens gratuitos al mes entre proveedores.
4. **Soporte MCP y A2A:** Interoperabilidad nativa con servidores MCP.

## Uso en Ecosistema de Antonio
- **Radar Comercial B2B:** Roteo masivo sin interrupciones para prospección en LinkedIn y Supabase.
- **CPS OS:** Fallback de baja latencia (<200ms) durante llamadas comerciales en vivo.
- **PayMind:** Agente de soporte técnico 24/7 sin caídas.
