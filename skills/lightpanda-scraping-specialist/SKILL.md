---
name: lightpanda-scraping-specialist
description: Diseña y ejecuta pipelines de web scraping, automatización browser efímera y extracción masiva de datos B2B usando Lightpanda Browser y PandaScript a ultra-alta velocidad y mínimo consumo de RAM.
---

# 🐼 Lightpanda Scraping & High-Speed Automation Specialist

Esta skill enseña al agente de IA a planificar y ejecutar extracción masiva de datos web y automatización de procesos utilizando **Lightpanda Browser** (el navegador headless ultra-rápido en Zig) y **PandaScript**.

---

## ⚡ 1. Cuándo usar Lightpanda vs Selenium/Chromium

Usar Lightpanda cuando el proyecto requiera:
* **Escalabilidad masiva:** Raspar cientos de sitios o prospectos de forma concurrente con mínimo uso de RAM (<50MB por instancia).
* **Dump directo a Markdown/HTML:** Convertir páginas SPA/JS a Markdown limpio para ingestión en pipelines de embeddings o LLMs.
* **Cero costo de tokens en producción:** Prototipar flujos con IA y exportar el script a **PandaScript** determínico.

---

## 🛠️ 2. Patrones de Ejecución

### Dump directo de URL a Markdown:
```bash
lightpanda fetch --dump markdown --wait-until networkidle0 "https://target-website.com"
```

### Servidor CDP (Puppeteer / Playwright Integration):
```javascript
import puppeteer from 'puppeteer-core';

const browser = await puppeteer.connect({
  browserWSEndpoint: "ws://127.0.0.1:9222"
});
const page = await browser.newPage();
await page.goto('https://target-website.com');
```
