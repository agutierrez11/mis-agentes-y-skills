---
name: agent-reach
description: B?squeda, scraping e inteligencia de mercado en tiempo real en m?s de 13 plataformas (Twitter/X, Reddit, LinkedIn, YouTube, GitHub, XiaoHongShu, Douyin, V2EX, RSS) sin requerir claves de API de pago, v?a CLI y servidor MCP.
---

# ?? Agent Reach ? No-API-Key Internet Intelligence

M?dulo de prospecci?n, monitoreo de redes y extracci?n de se?ales de mercado en tiempo real sin dependencia de claves de API de pago.

---

## ?? Capacidades Principales
- **Extracci?n de Se?ales y Quejas:** B?squeda en redes (Twitter/X, Reddit, LinkedIn) de quejas sobre clonaci?n de tarjetas, cobros duplicados en TPVs y problemas de pago de turistas en destinos vacacionales.
- **Prospecci?n B2B:** Identificaci?n de perfiles de l?deres gremiales (hoteler?a, restaurantes, agencias de viaje) y directores generales sin restricciones de API.
- **Transcripciones de YouTube:** Extracci?n de webinars, ponencias y an?lisis de competidores para an?lisis de inteligencia.
- **Compatibilidad MCP:** Servidor stdio MCP nativo para ser invocado por cualquier agente de Antigravity/Claude.

---

## ?? Comandos Operativos
```bash
# Diagn?stico de entorno
agent-reach doctor

# B?squeda de publicaciones en Twitter/X o Reddit
agent-reach search "fraude tarjeta cancun" --platform twitter,reddit --limit 20

# Extracci?n de transcripci?n de video de YouTube
agent-reach youtube --url "<VIDEO_URL>" --transcript

# B?squeda de perfiles de LinkedIn
agent-reach linkedin --search "Presidente CANIRAC Quintana Roo"
```

---

## ??? Mejores Pr?cticas
1. Normalizar siempre el texto extra?do (limpieza de emojis superfluos y codificaci?n UTF-8).
2. Combinar hallazgos con pipelines de an?lisis sem?ntico para clasificar quejas por severidad.
