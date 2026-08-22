---
name: figranium-browser-mcp
description: Guía de arquitectura e integración de Figranium para automatización visual de navegador Playwright, endpoints REST API y herramientas agénticas vía Model Context Protocol (MCP) para enriquecimiento BYOK a costo cero.
---

# 🤖 Figranium Browser MCP & Playwright Workflow Automation

## 📌 Propósito y Visión General
**Figranium** es un motor visual de automatización de navegador auto-hospedado (*self-hosted*) construido sobre **Playwright**. Permite diseñar flujos de scraping, navegación y extracción de datos mediante bloques visuales no-code/low-code y exponerlos instantáneamente como:
1. **Endpoints REST API** (`POST /api/v1/workflows/{id}/execute`).
2. **Servidores MCP (Model Context Protocol)** consumibles por células de agentes de IA en Antigravity.

---

## 🎯 Casos de Uso Core

### 1. Enriquecimiento BYOK a Costo Cero (Radar Comercial)
En lugar de consumir APIs de suscripción de alto costo (Apify, Lusha, Proxycurl):
- **Flujo**: Recibe `{"name": "Marc García", "company": "Klarna"}` -> Ejecuta búsqueda en Bing/Google SERP -> Extrae el puesto actual (`VP of Sales`) y rango de fechas (`2023 - Presente`) -> Retorna JSON estructurado.
- **Ventaja**: Cero riesgo de baneo (no toca la sesión de LinkedIn del usuario) y cero costo en créditos de terceros.

### 2. Pruebas de UI & QA Agéntico (Entorno Antigravity)
- Los agentes de la célula (`qa-expert`, `frontend-developer`) invocan workflows de Figranium vía MCP para verificar renderizado de páginas web, auditar flujos interactivos y extraer evidencias visuales.

---

## 🛠️ Arquitectura e Integración

### Configuración del Servidor Figranium (Docker / Self-Hosted)
```bash
docker run -d \
  --name figranium-server \
  -p 8080:8080 \
  -e PLAYWRIGHT_HEADLESS=true \
  -e ENABLE_MCP_SERVER=true \
  figranium/figranium:latest
```

### Protocolo MCP (Model Context Protocol)
El servidor de Figranium expone la herramienta MCP `execute_browser_workflow`:
```json
{
  "name": "execute_browser_workflow",
  "description": "Ejecuta un flujo de navegador Playwright en Figranium y retorna los datos extraídos.",
  "parameters": {
    "workflow_id": "enrich_linkedin_profile",
    "inputs": {
      "name": "Juan Pérez",
      "company": "Banco Falabella"
    }
  }
}
```

### Python Client Integration (FastAPI / Agent Cell)
```python
import requests

def enrich_contact_via_figranium(name: str, company: str) -> dict:
    url = "http://localhost:8080/api/v1/workflows/enrich_linkedin_profile/execute"
    payload = {
        "inputs": {
            "name": name,
            "company": company
        }
    }
    response = requests.post(url, json=payload, timeout=15)
    response.raise_for_status()
    return response.json().get("output", {})
```

---

## 🛡️ Reglas de Seguridad & Anti-Baneo
1. **No Inyectar Session Cookies (`li_at`)**: Toda extracción pública debe realizarse vía resultados de búsqueda indexados (Google/Bing SERP).
2. **Parsing de Fechas de Vigencia**: Filtrar siempre la etiqueta `Presente` / `Present` para certificar si el ejecutivo sigue activo en el cargo.
3. **Rate Limiting Local**: Aplicar esperas aleatorias (*jitter* de 200ms a 500ms) entre navegaciones.
