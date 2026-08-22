---
name: self-hosted-agent-orchestrator
description: Arquitectura, orquestación y despliegue de workspaces agénticos auto-hospedados (Self-Hosted AI Workspaces) con Docker y ejecución de tareas background inspirado en Odysseus.
---

# Skill: Self-Hosted Agent Orchestrator

## Propósito
Guiar el diseño, despliegue y administración de entornos agénticos auto-hospedados (Self-Hosted Agent Workspaces) en servidores VPS o infraestructura privada con contenedores Docker, bases de datos locales (PostgreSQL / SQLite) y ejecución persistente 24/7.

## Capacidades
1. **Despliegue Multi-Agente en Contenedores:**
   - Orquestación con `docker-compose` para aislar trabajadores agénticos, entornos de ejecución de navegador (Playwright/Puppeteer) y colas de tareas.
2. **Monitoreo & Logs en Vivo:**
   - Captura de trazas de ejecución, estado de tareas en segundo plano y métricas de consumo de tokens/recursos.
3. **Persistencia Local y Seguridad:**
   - Garantizar que los datos de prospectos, credenciales e historiales permanezcan dentro de la red privada sin exponerse a servicios de terceros no autorizados.
