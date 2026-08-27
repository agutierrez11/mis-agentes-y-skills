---
name: turbovec-high-compression-rag
description: Indexación vectorial hiper-comprimida hasta 16x con Rust y el algoritmo TurboQuant para RAG local de ultra-baja memoria basado en RyanCodrai/turbovec.
---

# Skill: Turbovec High-Compression RAG

## Propósito
Implementar índices vectoriales de ultra-alta velocidad y compresión extrema de memoria (hasta 16x de reducción sin pérdida apreciable de recall) usando Rust y el algoritmo **TurboQuant** (Google Research) para RAG local en agentes.

## Capacidades Principales
1. **Compresión Extrema sin Entrenamiento:**
   - Cuantización de vectores data-oblivious (convierte vectores float32 masivos en índices ultra-compactos sin requerir fases de entrenamiento).
2. **Aceleración SIMD (Rust Core):**
   - Ejecución mediante kernels optimizados en AVX-512 y ARM NEON para búsquedas vectoriales a velocidad nativa.
3. **Integración en Pipelines RAG Agénticos:**
   - Soporte para Python/Rust/PHP, habilitando bases de datos de conocimiento locales que caben en memoria RAM reducida.
