---
name: social-media-scraping
description: Extracción, scraping y enriquecimiento de datos en redes sociales (LinkedIn, Twitter/X, Instagram, TikTok, YouTube) para prospección B2B, inteligencia competitiva y monitoreo de mercado.
---

# 📱 Social Media Scraping & OSINT Intelligence Skill

Esta skill proporciona metodologías, patrones de arquitectura y catálogo de endpoints para la extracción automatizada y enriquecimiento de datos de redes sociales orientados a prospección comercial B2B, inteligencia de mercado y monitoreo de tendencias.

Basado en el ecosistema y catálogo curado de [`cporter202/social-media-scraping-apis`](https://github.com/cporter202/social-media-scraping-apis).

---

## 🎯 Casos de Uso Principales

1. **Prospección B2B & Generación de Leads:**
   * Enriquecimiento de perfiles ejecutivos (C-Level, VP, Directores de Pagos/Fintech).
   * Extracción de datos de empresas (tamaño de equipo, vacantes, tecnologías mencionadas).
   * Detección de cambios de puesto y actividad en LinkedIn.

2. **Monitoreo de Industria & Escucha Social:**
   * Rastreo de menciones de marcas, competidores y palabras clave en Twitter/X.
   * Monitoreo de feeds de noticias Fintech, Web3 y Pagos Digitales.
   * Extracción de videos, transcripciones y tendencias en TikTok / YouTube.

3. **Inteligencia de Precios & Competencia:**
   * Auditoría de campañas publicitarias y creativos activos (Meta Ad Library).
   * Análisis de engagement y tracción de competidores.

---

## 🛠️ Matriz de Plataformas y Métodos de Extracción

### 1. LinkedIn (B2B Lead Intelligence)
* **Datos Clave:** Perfil público, titular profesional, trayectoria laboral, empresa actual, publicaciones y comentarios.
* **Técnicas:**
  * Apify LinkedIn Scrapers / Voyager API interna (emulación de sesión).
  * Proxy rotativo residencial con limitación de tasa (rate limiting de 50-80 solicitudes/hora) para evitar bloqueos.
  * Extracción de listas de empleados por empresa y rol (*Headcount Intelligence*).

### 2. Twitter / X (Real-Time News & Sentiment)
* **Datos Clave:** Tweets por palabra clave/hashtag, perfiles de analistas, métricas de engagement (likes, retweets, replies).
* **Técnicas:**
  * Nitter instances / Syndication API endpoints.
  * GraphQL search queries con headers de emulación de cliente web.
  * Webhooks para alertas de eventos críticos (regulaciones Banxico, fusiones Fintech).

### 3. Instagram & TikTok (Media & Creator Trends)
* **Datos Clave:** Reels, TikToks, descripciones, hashtags, audios en tendencia, comentarios de usuarios.
* **Técnicas:**
  * Extracción de metadatos JSON a través de endpoints `?__a=1&__d=dis` o API de búsqueda de video.
  * Descarga y transcripción de audio (Whisper) para análisis de contenido.

### 4. YouTube (Video Data & Transcripts)
* **Datos Clave:** Títulos, descripciones, transcripciones completas (VTT/SRT), estadísticas del canal.
* **Técnicas:**
  * YouTube Data API v3 / `yt-dlp` para extracción de subtítulos y audio sin costo de cuota API.

---

## 📋 Protocolo de Extracción Ética y Resiliencia

1. **Rotación de Proxies:** Usar proxies residenciales para evitar baneos por IP.
2. **Backoff Exponencial y Delays Aleatorios:** Introducir retrasos (1.5s - 4.5s) con jitter entre peticiones.
3. **Normalización de Salida:**
   * Formatear siempre los resultados en JSON estructurado compatible con los datasets de los proyectos (ej. `fintechHubData.json`).
   * Limpiar caracteres especiales, acentos y validar URLs de perfiles.
