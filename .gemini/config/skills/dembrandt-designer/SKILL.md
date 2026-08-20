---
name: dembrandt-designer
description: Extracci?n e ingenier?a inversa de Design Systems de cualquier sitio web en producci?n mediante Playwright headless, generando tokens W3C/JSON, variables CSS calculadas, fuentes, paletas de color y detecci?n de design drift.
---

# ?? Dembrandt ? Web Design System Reverse Engineering

Herramienta de extracci?n automatizada de tokens de dise?o y sistemas visuales a partir de sitios web en vivo.

---

## ?? Flujo de Trabajo
1. **Ejecuci?n Headless con Playwright:** Renderiza el DOM completo ejecutando JavaScript y evaluando estilos calculados (`getComputedStyle`).
2. **Extracci?n de Tokens:**
   - **Paleta de Color:** Colores primarios, secundarios, neutros y de estado con sus valores HEX, RGB y HSL.
   - **Tipograf?a:** Familias de fuentes, pesos (`font-weight`), alturas de l?nea (`line-height`) y escalas de tama?o.
   - **Espaciado y Radios:** Escalas de padding/margin, border-radius y sombras (`box-shadow`).
3. **Formato W3C Design Tokens:** Exportaci?n estructurada en JSON para importaci?n directa en Figma, CSS o Tailwind.

---

## ?? Uso en Terminal / Scripts
```bash
# Extraer sistema de dise?o completo de un sitio web
npx dembrandt https://ejemplo-fintech.com --output ./design-tokens.json

# Extraer ?nicamente paleta de colores y variables CSS
npx dembrandt https://banxico.org.mx --extract colors,css-vars
```

---

## ?? Aplicaciones Clave
- **Auditor?as de Competencia:** Desglosar c?mo construyen su UI plataformas l?deres como Wise, Nubank, Stripe o DLocal.
- **Control de Design Drift:** Detectar inconsistencias visuales en builds de CI/CD comparando contra un snapshot base.
