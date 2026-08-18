---
name: obsidian-clipper
description: Ingesta web automatizada, extracción estructurada de metadatos (Schema.org, OpenGraph) y plantillas Markdown para Obsidian Vaults usando obsidian-clipper (obsidianmd/obsidian-clipper).
---

# ✂️ Obsidian Web Clipper — Structured Markdown Ingestion

Esta habilidad define los flujos de trabajo para capturar, limpiar y estructurar información desde la web hacia bóvedas de conocimiento (Obsidian Vaults) utilizando el **Obsidian Web Clipper oficial** (`obsidianmd/obsidian-clipper`).

## 🔑 Capacidades Principales
1. **Extracción Limpia a Markdown:** Conversión de páginas completas, artículos, hilos y posts a Markdown puro sin código innecesario ni tracking.
2. **Extracción de Metadatos Semánticos:** Mapeo automático de propiedades desde `OpenGraph`, `Schema.org JSON-LD` y selectores CSS.
3. **Reglas de Plantillas por Dominio:**
   - **LinkedIn Posts / Artículos:** Captura autor, fecha, métricas y texto limpio para prospección comercial.
   - **Papers y Noticias Financieras:** Captura título, resumen, fuentes citadas y etiquetas taxonómicas.
4. **Almacenamiento Local-First:** Ingesta directa en archivos locales `.md` listos para ser indexados por grafos de conocimiento o RAG.

## 🛠️ Buenas Prácticas de Estructuración
* **Frontmatter Estándar:** Cada nota capturada debe incluir metadatos mínimos:
  ```yaml
  ---
  title: "{{title}}"
  source: "{{url}}"
  author: "{{author}}"
  date_clipped: "{{date}}"
  tags: [investigacion, fintech, pagos]
  ---
  ```
* **Conexión Relacional:** Añadir enlaces de doble corchete `[[Entidad]]` para integrar la nota automáticamente con el grafo relacional de la bóveda.
