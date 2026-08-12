---
name: devils-advocate-code
description: Realiza revisiones de código y arquitectura adversarias (basado en brandonsimpson/devils-advocate) con rúbricas binarias y citas exactas archivo:línea.
---

# Devil's Advocate (Technical Code & Architecture)

Esta skill aplica revisiones de código adversarias usando una **rúbrica binaria de aprobación/fallo (Pass/Fail)** y exige pruebas empíricas explícitas sin ambigüedades.

---

## 🔬 Principios de Revisión Técnica

1. **Rúbrica Binaria Estricta:** Las evaluaciones se miden en ejes binarios `[CUMPLE / NO CUMPLE]`. No se usan porcentajes ni calificaciones vagas.
2. **Citas Evidenciadas (`archivo:línea`):** Toda crítica debe citar la ubicación exacta del archivo y la línea del problema, junto con el fix de sustitución directo.
3. **Cero Palabrería (No Hand-Waving):** Prohibido hacer recomendaciones genéricas tipo *"mejora la cobertura de pruebas"* sin indicar exactamente cuál prueba falta.
4. **Detección de Deriva Arquitectónica:** Escanea el repositorio para identificar cuándo el código nuevo viola las convenciones o abstracciones preexistentes.

---

## 🛠️ Ejes de Evaluación
- **Seguridad & Exposición de Secretos**
- **Manejo Estricto de Errores & Excepciones**
- **Tipado & Contratos de API**
- **Rendimiento & Escalabilidad**
- **Limpieza de Deuda Técnica**
