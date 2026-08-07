# 🔀 Multiplayer Agent Orchestrator (`multiplayer-agent-orchestrator`)

Esta skill proporciona las pautas de diseño, arquitectura e implementación para construir y desplegar **Flotas de Agentes Colaborativas Multi-Usuario (Multiplayer AI Agent Harnesses)** con aislamiento estricto de sandboxes, credenciales y estados.

Inspirado en la arquitectura open-source de **`yc-software/qm`** (Quartermaster).

---

## 📌 ¿Cuándo usar esta Skill?

- Al construir aplicaciones SaaS B2B donde **múltiples usuarios o equipos** interactúan simultáneamente con agentes de IA.
- Cuando se requiera integración multi-canal (Slack, WhatsApp, Dashboard Web) manteniendo sesiones e historiales independientes.
- Para desplegar infraestructuras agénticas *Self-Hosted* privadas en Kubernetes, Fly.io, AWS o servidores locales.

---

## 🏗️ Arquitectura General del Sistema

```
[ Slack / Web UI / WhatsApp ]
           │
           ▼
  [ Fastify / Node API ] ─── (Auth & Rate Limit)
           │
  ┌────────┴────────┐
  ▼                 ▼
[ User Silo 1 ]   [ User Silo 2 ]
 ├─ Credentials    ├─ Credentials
 ├─ Memory Store   ├─ Memory Store
 └─ Sandbox Exec   └─ Sandbox Exec
```

---

## 🛡️ Principios y Reglas de Diseño

### 1. Aislamiento Estricto por Usuario (User Sandboxing)
- **Zero Data Leakage:** Ningún usuario o agente debe tener acceso a las memorias, archivos temporales o credenciales de otro usuario.
- Cada workspace debe instanciarse con un UUID único y un almacén de contexto completamente aislado.

### 2. Persistencia decoupled (Fastify + PostgreSQL/Redis)
- Almacenar el historial de conversación y los checkpoints de ejecución en PostgreSQL/Redis en lugar de memoria volatil.
- Permitir la reanudación asíncrona de agentes si el servidor o contenedor se reinicia.

### 3. Orquestación Multi-Canal (Slack / Web / API)
- Desacoplar la lógica agéntica del canal de presentación.
- El agente emite eventos (stream de tokens, tool calls, status updates) que se transmiten al canal activo del usuario vía WebSockets o Server-Sent Events (SSE).

### 4. Gestión de Credenciales por Silo
- Las claves de API (OpenAI, Gemini, CRMs) se encriptan individualmente por usuario/organización.
- El agente solo puede solicitar permisos para acciones autorizadas dentro del ámbito del usuario autenticado.
