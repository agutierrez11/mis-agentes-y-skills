---
name: agentic-cms-architect
description: Diseña, maqueta y despliega sitios web estáticos, landing pages y sistemas de contenidos agénticos ligeros con cero runtime usando arquitectura HTML/CSS pura y el paradigma Instatic.
---

# 🌐 Agentic CMS & Static Site Architect (Instatic Paradigm)

Esta skill permite al agente de IA diseñar, maquetar, estructurar y desplegar sitios web estáticos de alta velocidad, landing pages comerciales y portales de contenidos sin depender de frameworks pesados de JS (React, Next.js) cuando el proyecto requiere carga ultra-rápida, cero runtime y compatibilidad total con servidores ligeros.

---

## 🎨 1. Arquitectura de Diseño y Tokens en HTML/CSS Puro

Para garantizar que los sitios web luzcan de nivel profesional B2B y carguen al instante:

### Tokens de Diseño en CSS Vars (Fidelidad Instatic / Core Framework):
```css
:root {
  --color-primary: #2563EB;
  --color-primary-dark: #1D4ED8;
  --color-bg-main: #0F172A;
  --color-bg-card: #1E293B;
  --color-text-main: #F8FAFC;
  --color-text-muted: #94A3B8;
  --font-family-sans: 'Outfit', -apple-system, sans-serif;
  --font-family-mono: 'JetBrains Mono', monospace;
  --border-radius-card: 14px;
}
```

### Reglas de Estructuración HTML:
1. **Semántica Estricta:** Uso obligatorio de `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`.
2. **Zero Div-Soup:** Mantener la jerarquía de etiquetas limpia, readable en `view-source` y optimizada para SEO.
3. **Cero Dependencias de Runtime JS:** La interactividad básica (calculadoras, modales, pestañas) debe ser ligera en Vanilla JS nativo de menos de 10KB.

---

## 🧱 2. Módulos y Reusabilidad de Componentes

### Componentes Reutilizables:
* **Cards de KPIs:** Tarjetas con bordes con gradiente sutil y tipografía monospace para cifras.
* **Calculadoras en Tiempo Real:** Interacciones con `input range` (sliders) y recálculo instantáneo de valores en el DOM sin re-renders costosos.
* **Tablas de Comparación TCO:** Tablas limpias con contrastes de color para resaltar ventajas comerciales.

---

## 🚀 3. Flujo de Trabajo para Creación de Sitios Estáticos Agénticos

1. **Diseñar el Layout y Tokens:** Crear la paleta HSL y tipografías en el CSS principal.
2. **Construir Secciones Semánticas:** Maquetar el contenido con enfoque en velocidad de conversión B2B.
3. **Optimización de Assets & Despliegue:** Generar un output listo para GitHub Pages, Cloudflare Pages o Docker/Caddy.
