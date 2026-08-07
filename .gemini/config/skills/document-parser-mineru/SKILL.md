---
name: document-parser-mineru
description: Extrae y parsea archivos PDF complejos, escaneos, contratos y reportes contables/regulatorios a Markdown estructurado conservando tablas y fórmulas.
---

# 📄 Skill: Document Parser MinerU (PDF to Markdown Engine)

Esta habilidad capacita a los agentes de Antigravity para ingerir, estructurar y extraer información limpia de documentos complejos en formato PDF (reportes de la CNBV, estados financieros de SOFOMes, contratos de arrendamiento, presentaciones escaneadas o especificaciones técnicas).

---

## 📌 Cuándo usar esta Skill

Usa esta skill cuando el usuario o un agente necesite:
1. Extraer tablas financieras o anexos regulatorio-contables de archivos PDF pesados sin perder la alineación de columnas.
2. Convertir un contrato largo o propuesta comercial en Markdown estructurado para análisis de riesgos legales o Due Diligence.
3. Procesar especificaciones de APIs o manuales de arquitectura bancaria escaneados.

---

## ⚙️ Capacidades Principales

- **Preservación de Estructura:** Convierte títulos, subtítulos, listas y notas al pie respetando la jerarquía original.
- **Extracción de Tablas Finas:** Extrae tablas complejas en formato Markdown o HTML embebido sin fusionar celdas incorrectamente.
- **Fórmulas y Ecuaciones:** Convierte fórmulas matemáticas a notación LaTeX (`$...$` o `$$...$$`).
- **Filtrado de Ruido:** Elimina encabezados repetitivos, números de página y marcas de agua.

---

## 📋 Protocolo de Extracción para Análisis Financiero / B2B

Cuando utilices esta skill para extraer datos de reportes bancarios o prospectos B2B, sigue estas etapas:

1. **Identificación de Secciones Clave:** Priorizar la extracción de Tablas de Margen Financiero, Cartera Vencida y Anexos de Cumplimiento PLD/FT.
2. **Formateo Estricto:** Representar todas las cifras monetarias en su moneda original (ej. MXN o USD) con dos decimales.
3. **Etiquetado de Incerteza:** Si una cifra en el PDF escaneado resulta ilegible o ambigua debido a la resolución, marcarla explícitamente como `<!-- PENDIENTE: verificar en fuente original -->`.
