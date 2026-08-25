---
name: ecc-agent-harness
description: Harness de optimización de rendimiento para agentes de IA (basado en affaan-m/ecc). Establece desarrollo research-first, protocolos Zero-Assumption, instintos de conducta inmutables y memoria de arnés para evitar alucinaciones de backend y pérdida de estado.
---

# ECC Agent Harness — Optimization & Instinct Control System

Este skill implementa los patrones de diseño de **affaan-m/ecc** (Explicit Agent Harness Performance Optimization System) para garantizar máxima precisión, cero asunciones y persistencia estricta de estado en proyectos de alta complejidad.

---

## 🛡️ Principios Fundamentales (Instincts)

1. **Research-First Mandate:**
   - Queda strictly prohibido realizar modificaciones en el código o proponer arquitecturas sin inspeccionar antes el código fuente real, schemas y archivos de configuración locales.

2. **Protocolo Zero-Assumption (Cero Asunciones):**
   - Prohibido asumir que una API, tabla de base de datos (Supabase) o servicio backend está "conectado" o "listo" basándose solo en nombres de archivos o funciones.
   - Todo estado backend debe etiquetarse como `CONTRADICHO` o `NO VERIFICADO` hasta ejecutar una comprobación empírica en caliente.

3. **Memoria de Arnés y Persistencia de Estado:**
   - La depuración del usuario (contactos descartados, notas, cambios en CRM) prevalece sobre datasets crudos o demos.
   - Cada modificación debe sincronizar IndexedDB / LocalStorage / Backend de inmediato para evitar la memoria de teflón.

---

## 🔄 Flujo de Trabajo ECC

```text
1. FASE DE INVESTIGACIÓN (Research)
   ↳ Inspección silenciosa de archivos locales (.env, schema, index.html)
   ↳ Detección de discrepancias y dependencias

2. PLANTEAMIENTO Y VERIFICACIÓN EMPÍRICA
   ↳ Ejecución de scripts de prueba (HTTP / Python audit)
   ↳ Registro de códigos de respuesta reales (HTTP 200 vs HTTP 404)

3. EJECUCIÓN CONTROLADA Y LOGGING
   ↳ Edición incremental sin alterar contratos API existentes
   ↳ Auto-sincronización y persistencia inmediata

4. AUDITORÍA Y ENTREGA
   ↳ Verificación empírica post-ejecución
   ↳ Confirmación de CI/CD (git push)
```
