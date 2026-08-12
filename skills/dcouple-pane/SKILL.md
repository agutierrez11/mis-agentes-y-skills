---
name: dcouple-pane
description: Orquestación de agentes de IA en paralelo en terminales y gestión de paneles de trabajo independientes con CLI runpane (dcouple/Pane).
---

# 🖥️ Pane — Terminal-First Multi-Agent Orchestrator

Esta habilidad le permite a Antigravity y a sus subagentes orquestar ejecuciones paralelas de agentes CLI utilizando **Pane** (`github.com/dcouple/Pane`) y el CLI `runpane`.

## 🔑 Características Principales
1. **Multi-Agent Orchestration:** Ejecución simultánea de agentes en múltiples paneles/pestañas de terminal en Windows, macOS y Linux.
2. **Cross-Terminal `@mentions`:** Comunicación y extracción de líneas de código o logs entre terminales independientes (ej. `@panel2` lee la salida de la terminal 2).
3. **Persistent Terminal Workspaces:** Espacios de trabajo persistentes para mantener agentes corriendo tareas de larga duración.

## 🛠️ Comandos CLI `runpane`
```bash
# Registrar repositorio y descubrir esquema de comandos
runpane register

# Listar paneles activos y agentes en ejecución
runpane list

# Mencionar y extraer contexto de otro panel
runpane context @panel2
```

## 🎯 Protocolo de Uso en Antigravity
- Usar `Pane` cuando se requiera dividir el trabajo técnico en paneles independientes (ej. Panel 1: Frontend/UI, Panel 2: Backend/FastAPI, Panel 3: QA/Auditores).
