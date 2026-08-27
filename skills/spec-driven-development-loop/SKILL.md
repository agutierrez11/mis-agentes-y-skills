---
name: spec-driven-development-loop
description: Bucle de desarrollo guiado por especificaciones (Spec-Driven Development / Smart Ralph) para investigación previa, diseño riguroso y ejecución iterativa comprobada.
---

# Skill: Spec-Driven Development Loop (Smart Ralph)

## Propósito
Eliminar ejecuciones precipitadas ("a lo loco"), parches superficiales y alucinaciones en el código mediante un proceso estructurado en 4 fases estrictas con validación empírica previa a la modificación de la base de código.

## Las 4 Fases de Desarrollo

### 1. Fase de Investigación (Research & Codebase Inspection)
- **Regla de Oro:** **PROHIBIDO modificar código o ejecutar comandos destructivos durante la investigación.**
- Inspeccionar el código authoritative, configuraciones locales (`package.json`, `AGENTS.md`, `.env`), firmas exactas de funciones y logs reales de error.
- Prohibido asumir nombres de variables, rutas de archivos o comportamientos de APIs de terceros.

### 2. Fase de Especificaciones & Criterios de Aceptación (Requirements)
- Definir explícitamente qué problema se está resolviendo y los criterios de aceptación medibles.
- Si faltan datos o hay incertidumbre, declarar las dudas abiertamente en lugar de inventar o adivinar métricas/parámetros.

### 3. Fase de Diseño & Planificación (Architecture & Design)
- Estructurar el plan de implementación paso a paso antes de tocar código.
- Identificar dependencias, posibles impactos colaterales y manejo estructurado de errores.

### 4. Fase de Ejecución Iterativa & Prueba de Vida (Proof of Execution)
- Ejecutar el plan paso a paso de forma secuencial.
- **Prueba de Vida Obligatoria:** Ninguna tarea se reporta como "lista" o "completada" sin mostrar el output real de la consola, logs o pruebas automatizadas que confirmen su éxito empírico.
- Si un comando o prueba falla, investigar la causa raíz en lugar de tragar excepciones o aplicar parches sintomáticos.
