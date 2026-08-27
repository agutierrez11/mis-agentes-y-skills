---
name: typescript-tdd-refactoring-pro
description: Disciplina de tipado estricto en TypeScript/React, desarrollo guiado por pruebas (TDD), refactorización limpia y prevención de entropía inspirado en Matt Pocock.
---

# Skill: TypeScript TDD & Refactoring Pro

## Propósito
Garantizar la máxima calidad en proyectos TypeScript/Node.js/React mediante patrones avanzados de tipado (generics estrictos, discriminated unions), desarrollo guiado por pruebas (TDD) y refactorizaciones modulares.

## Pautas de Código
1. **Tipado Estricto (Zero Any):**
   - Prohibido el uso de `any`. Preferir `unknown`, interfaces explícitas y utilidades tipo `Zod` para validación en runtime de entradas externas.
2. **Ciclo TDD (Red-Green-Refactor):**
   - Escribir pruebas unitarias/integración que fallen antes de implementar la solución de código.
3. **Refactorización Segura:**
   - Modificar bloques de código preservando contratos existentes sin romper llamadas dependientes.
