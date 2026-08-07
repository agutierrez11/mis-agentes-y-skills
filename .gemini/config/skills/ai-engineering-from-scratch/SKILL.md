---
name: ai-engineering-from-scratch
description: Referencia completa y patrones de diseño de IA desde cero (Fundamentos, LLMs, Agentes y Multi-Agente) basados en el currículum de rohitg00/ai-engineering-from-scratch.
---

# AI Engineering From Scratch — Reference Skill

Esta skill sirve como guía y referencia de ingeniería para la célula de agentes de Antigravity al diseñar o auditar flujos agénticos, clasificación semántica, evaluación de LLMs e infraestructura de IA.

---

## 📌 Principios de Diseño
1. **Comprensión "From Scratch":** Entender la mecánica matemática subyacente (embeddings, atención, cuantización) antes de sugerir abstracciones.
2. **Evaluadores Cero-Sesgo (LLM-as-a-Judge):** Construcción de evaluadores sin dependencias pesadas para medir calidad de respuestas.
3. **Multi-Agent Swarms:** Patrones deterministas para orquestación de agentes con roles definidos y loops de realimentación.

---

## 🛠️ Áreas de Referencia

### 1. Embeddings y Clasificación Semántica
- Normalización estricta de cadenas (minúsculas, remoción de diacríticos y acentos).
- Cálculo de similitud cosenoidal a bajo nivel para matching de entidades sin latencia externa.

### 2. Orquestación Agéntica
- Enrutamiento de tareas por capacidades.
- Arquitectura de agentes con estado y memoria de contexto eficiente.

### 3. Buenas Prácticas de Evaluación
- Métricas de precisión, cobertura y latencia para modelos en producción.
