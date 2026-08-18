---
name: deepseek-harness
description: Orquestación de runtimes y bucles agénticos modulares basados en DeepSeek Harness (deepseek-ai/deepseek-harness) y el meta-framework Cordis.
---

# 🧠 DeepSeek Harness (DSH) — Modular Agent Runtime Framework

Esta habilidad guía la arquitectura, configuración y despliegue de agentes autónomos utilizando el framework **DeepSeek Harness** (`deepseek-ai/deepseek-harness`).

## 🔑 Filosofía: "Everything is a Plugin"
DeepSeek Harness desacopla todos los componentes de un sistema agéntico en plugins independientes construidos sobre **Cordis** (meta-framework de componibilidad espaciotemporal):
1. **Model Layer:** Modelos intercambiables en caliente (DeepSeek V3/R1, Claude, GPT, modelos locales).
2. **Tools Layer:** Herramientas modulares de búsqueda, scraping, ejecución de código y APIs de negocio.
3. **Session Management:** Gestión persistente de hilos de conversación, memoria y checkpoints.
4. **Agent Loop:** Lógica de planificación, razonamiento y toma de decisiones desacoplada.

## 🛠️ Modos de Ejecución
* **Modo Web UI (Quickstart):**
  ```bash
  npx @deepseek-ai/dsh web
  ```
* **Instalación desde Fuentes:**
  ```bash
  git clone https://github.com/deepseek-ai/deepseek-harness.git
  cd deepseek-harness
  pnpm install
  pnpm run build
  pnpm dsh web
  ```

## 📋 Reglas de Integración en el Ecosistema
- **Plugins Taggeados:** Diseñar extensiones compatibles con la etiqueta `dsh-plugin`.
- **Componibilidad Segura:** Mantener las herramientas desacopladas del modelo para permitir swapping instantáneo sin alterar la lógica de negocio.
- **Trazabilidad:** Registrar eventos y pasos del loop para auditorías y depuración sistemática.
