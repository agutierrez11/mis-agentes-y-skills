---
name: ai-engineering-from-scratch
description: Referencia completa y patrones de diseño de IA desde cero (Fundamentos, LLMs, Agentes y Multi-Agente) basados en el currículum de rohitg00/ai-engineering-from-scratch.
---

# 🧠 AI Engineering From Scratch (Curriculum & Design Patterns)

Esta skill permite a la célula de agentes consultar, diseñar e implementar patrones de ingeniería de Inteligencia Artificial desde los principios fundamentales ("from scratch"), cubriendo desde matemáticas de deep learning y arquitectura de LLMs hasta orquestación de agentes y evaluación sin sesgo.

---

## 📚 1. Fases del Currículum de Referencia

1. **Fundamentos Matemáticos & ML Puro:**
   - Cálculo diferencial, álgebra lineal y tensores implementados desde cero.
   - Algoritmos de optimización (SGD, Adam) y retropropagación manual.
2. **Deep Learning & Transformers:**
   - Mecanismos de atención (Self-Attention, Multi-Head Attention).
   - Positional Encodings y arquitectura Encoder-Decoder.
3. **LLMs & Fine-Tuning:**
   - Tokenización (BPE, WordPiece).
   - Cuantización (LoRA, QLoRA) y ajuste fino eficiente de parámetros (PEFT).
4. **Agentic Engineering & Multi-Agent Swarms:**
   - Orquestación de agentes autónomos con loops de realimentación y memoria de contexto.
   - Patrones de deliberación (LLM Council, LLM-as-a-Judge) para evaluación sin sesgo.

---

## 🛠️ 2. Guía de Aplicación en Agentes

- **Sin Abstracciones Pesadas:** Preferir implementaciones livianas en Python/TypeScript para tareas de normalización, clasificación o embeddings simples.
- **Evaluación Autónoma:** Implementar validadores deterministas para medir latencia, precisión y alucinaciones en respuestas agénticas.
- **Enrutamiento Agéntico:** Organizar agentes en enjambres (swarms) especializados según la complejidad de la tarea.
