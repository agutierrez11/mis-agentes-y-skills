---
name: loopx-agent-kernel
description: Gestión de ejecuciones autónomas de larga duración, loops agénticos duraderos y kernels de estado para células de agentes usando LoopX (huangruiteng/loopx).
---

# 🔄 LoopX — Lightweight Agent Loop Engineering Kernel

Esta habilidad establece patrones para ejecutar células de agentes de IA en ciclos continuos (*long-running loops*) de forma segura usando **LoopX** (`github.com/huangruiteng/loopx`).

## 🔑 Características Principales
1. **Durable Goals:** Los objetivos principales del agente persisten incluso tras reinicios o fallas del sistema.
2. **Executable ToDos:** Gestión de listas de tareas activas que se evalúan progresivamente.
3. **Evidence Logs:** Registros de comprobación empírica para verificar que una tarea fue completada antes de pasar a la siguiente.
4. **Quota-Aware Auto-Wake:** Control del límite de tokens y costos con activación por temporizador.

## 🛠️ Patrón de Trabajo en Antigravity
- **Tareas Overnight:** Utilizar LoopX para delegar auditorías masivas de prospectos o investigación de mercado sin perder el contexto ni caer en bucles infintos.
- **Checkpoints:** Registrar logs de evidencia en cada iteración del loop antes de dar por terminada una meta comercial.
