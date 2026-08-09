---
name: warden-agent-orchestrator
description: Orquestaci?n de agentes aut?nomos locales con bucle de auto-modificaci?n de c?digo, sub-agentes especializados (Atlas, Iris, Dexter, Byte), deliberaci?n colegiada multi-modelo (The Council) y control de sesiones activas en Chrome.
---

# ??? Warden ? Local Autonomous Agent Orchestrator

Arquitectura y patrones de orquestaci?n de agentes aut?nomos locales con capacidad de ejecuci?n de tareas complejas, control de navegador e introspecci?n de c?digo.

---

## ??? Estructura Multi-Agente
- **Atlas:** Navegaci?n web avanzada mediante Playwright y ejecuci?n segura de comandos de terminal.
- **Iris:** Automatizaci?n de canales de comunicaci?n (correos IMAP/SMTP, mensajer?a y calendarios CalDAV).
- **Dexter & Byte:** Gesti?n de colas de tareas, cronogramas y seguimiento continuo de proyectos.
- **The Council:** Mecanismo de deliberaci?n multi-modelo donde varios LLMs debaten y consens?an antes de ejecutar acciones de alto impacto.

---

## ?? Protocolos de Seguridad y Confinamiento
1. **Ejecuci?n en Sandboxing:** Siempre aislar procesos con acceso a shell en contenedores Docker o entornos virtuales.
2. **Guardrails de Auto-Modificaci?n:** Exigir validaci?n de tests y linters antes de que cualquier agente reinicie servicios o aplique cambios en su propio c?digo fuente.
