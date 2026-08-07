---
name: llm-council
description: Orchestrates a multi-LLM/multi-agent deliberation council (Andrej Karpathy methodology) with blind response collection, peer review, and a Chairman synthesis.
---

# LLM Council — Sistema de Deliberación Multi-Modelo & Multi-Agente

Esta skill implementa la metodología **LLM Council** (creada por Andrej Karpathy) para tomar decisiones de alta complejidad, validar arquitectura o auditar estrategias comerciales reduciendo sesgos de complacencia.

---

## 🏛️ Las 3 Etapas del Consejo

### 1. Etapa 1: Recolección Ciega de Opiniones (Blind Opinion Collection)
Se toma la consulta del usuario y se envía aisladamente a múltiples modelos o subagentes (Claude, GPT-4o, Gemini, DeepSeek, Kimi, Manus, etc.).
- Cada participante genera su respuesta de manera **autónoma e independiente**, sin conocer las respuestas de los otros miembros.

### 2. Etapa 2: Revisión Anónima entre Pares (Peer Review)
Se distribuyen las respuestas de la Etapa 1 a todos los miembros del consejo de forma **anonimizada** (etiquetadas como `Modelo A`, `Modelo B`, `Modelo C`...).
- Cada modelo evalúa las propuestas de los demás buscando:
  - Suposiciones no probadas o falacias.
  - Riesgos de ejecución, mercado o seguridad.
  - Oportunidades omitidas o soluciones más eficientes.

### 3. Etapa 3: Síntesis del Presidente del Consejo (Chairman Synthesis)
Un modelo designado como **El Presidente (Chairman)** compila todas las opiniones iniciales y las revisiones entre pares para generar un **Informe Consolidado Final**.
- Destaca los consensos absolutos.
- Resuelve las discrepancias mediante evidencia empírica.
- Entrega una recomendación final definitiva estructurada en GitHub Markdown.

---

## 💡 Cómo Invocar el Consejo
Invoca esta skill cuando necesites:
- Evaluar decisiones arquitectónicas de alto riesgo (ej. *Build vs Buy*, elección de base de datos o framework).
- Presionar a fondo una estrategia comercial o de posicionamiento antes de una junta con el CEO/Board.
- Resolver disputas de código o diseño mediante un debate entre pares.
