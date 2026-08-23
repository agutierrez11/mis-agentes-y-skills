---
name: loop-engineering
description: Practical patterns, starters, CLI tools and execution loops for AI coding agents and agentic cells based on cobusgreyling/loop-engineering.
---

# Loop Engineering — Patrones de Bucles Agénticos para Agentes de IA

Este skill define la metodología y los patrones tácticos de **Loop Engineering** (Ingeniería de Bucles Agénticos) para células de agentes en Antigravity. Permite ejecutar flujos autónomos de larga duración, mantener kernels de estado y recuperarse de fallos sin perder contexto.

---

## 🎯 Principios Fundamentales del Loop Engineering

1. **Estado Explícito y Persistente (State Kernel):**
   - El agente debe leer el estado actual (state.json o base de datos) al inicio de cada iteración del bucle.
   - Toda mutación de estado debe ser atómica y verificable.

2. **Bucle de Retroalimentación Autónoma (Feedback Loop):**
   - **Plan → Execute → Verify → Adjust**.
   - No se declara un bucle completado sin ejecutar un comando de verificación empírica (ej. linters, tests automatizados, HTTP status checks).

3. **Resiliencia & Fail-Safe:**
   - Si un paso del bucle falla (ej. timeout de API, error de sintaxis), el bucle retrocede al último estado seguro (*rollback*) o ejecuta una ruta de contingencia en lugar de abortar la ejecución completa.

4. **Context Window Protection:**
   - Para bucles de larga duración, se deben resumir los artefactos y logs en archivos de disco en lugar de acumular salidas extensas en la memoria de la ventana de chat.

---

## 📋 Lista de Verificación para Agentes en un Loop

- [ ] ¿El kernel de estado está actualizado en disco antes de tomar decisiones?
- [ ] ¿La condición de salida del bucle es cuantitativa y medible?
- [ ] ¿Se verificaron los logs de ejecución tras cada cambio?
- [ ] ¿Se realizó git commit al completar un hito del bucle?

---

## 🔗 Referencias y Fuentes

- **Repositorio original de inspiración:** [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)
- **Autor:** Cobus Greyling (AI Agent & Loop Engineering Patterns)
