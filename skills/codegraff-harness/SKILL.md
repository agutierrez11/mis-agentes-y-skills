---
name: codegraff-harness
description: Motor agéntico de desarrollo y ciclo de evaluación continua DGM (basado en justrach/codegraff). Exige validación empírica en vivo antes de declarar finalizada cualquier tarea, soportando integraciones MCP y ejecución distribuida multi-proveedor.
---

# CodeGraff Harness — Continuous Evolution & Verification Loop

Este skill adopta la arquitectura de **justrach/codegraff** (`graff`) para la ejecución autónoma con auto-evaluación continua (DGM Evolution Loop) y verificación pre/post ejecución.

---

## 🔁 DGM Evolution Loop (Ciclo de Verificación Obligatorio)

1. **Pre-Flight Snapshot:**
   - Antes de aplicar un cambio en archivos críticos (`index.html`, backend APIs), registrar el estado baseline y las afirmaciones a probar.

2. **Ejecución de Cambios Scoped:**
   - Limitar las ediciones al alcance exacto del problema sin modificar módulos no relacionados.

3. **Post-Flight Live Verification:**
   - Ninguna tarea se marca como completada sin ejecutar comandos de verificación en caliente (Playwright screenshots, scripts Python audit, peticiones HTTP REST).
   - Si la prueba falla o devuelve un error (ej. `HTTP 404`), el ciclo entra en auto-corrección sin reportar éxito falso.

---

## ⚡ Reglas de Robustez MCP y Backend

- **Tratamiento de Excepciones:** Queda prohibido tragar excepciones silenciosamente (`try ... catch {}` sin logging o fallbacks ficticios). Todo fallo debe ser expuesto limpiamente.
- **Trazabilidad Total:** Registrar logs claros en terminal y consola cuando se interactúa con APIs externas (HarvestAPI, Apify, Supabase).
- **Despliegue CI/CD Continuo:** Ejecutar `git commit` y `git push` después de cada hito verificado para mantener el pipeline activo.
