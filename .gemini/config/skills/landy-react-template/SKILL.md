---
name: landy-react-template
description: >
  Template de landing page React open-source, profesional y rápida (Google Lighthouse perfecto).
  Usa cuando el usuario quiera crear una landing page para startup, producto o proyecto con React/TypeScript.
  Soporta i18n, routing por archivos, formulario de contacto y animaciones suaves.
  Repo: https://github.com/Adrinlol/landy-react-template
---

# Landy React Template

**Repo:** https://github.com/Adrinlol/landy-react-template  
**Demo:** https://adrinlol.github.io/landy-react-template/  
**Stack:** React + TypeScript (sin dependencias de terceros)  
**Lighthouse:** Perfecto en Performance, Accessibility, Best Practices y SEO

---

## Cuándo usar esta Skill

- Usuario pide landing page profesional con React
- Necesita soporte multi-idioma (i18n nativo)
- Quiere Lighthouse score perfecto sin configuración manual
- Proyecto nuevo de startup, SaaS o herramienta para desarrolladores

---

## 🚀 Instalación

```bash
git clone https://github.com/Adrinlol/landy-react-template.git my-landing
cd my-landing
npm install
npm start        # dev server
npm run build    # producción
```

## 📁 Estructura de Archivos Clave

```
src/
├── pages/           # Cada archivo = una ruta automática
├── components/      # Componentes reutilizables (Header, Footer, Hero, etc.)
├── content/         # ⭐ Todo el texto en JSON — editar sin tocar React
│   ├── en/          # Inglés
│   └── es/          # Español
└── styles/          # CSS global
```

## ✏️ Cómo personalizar (sin conocer React)

**Solo editar los JSON de contenido:**

```json
// src/content/en/homeContent.json
{
  "hero": {
    "title": "Tu Producto Aquí",
    "subtitle": "Descripción en una línea",
    "button": "Empieza Gratis"
  },
  "about": {
    "title": "Sobre Nosotros",
    "content": "..."
  }
}
```

## 🎨 Características de Diseño

- **Sin modo oscuro forzado** — tema claro por defecto
- **Animaciones suaves** — CSS transitions, sin libraries pesadas
- **Responsive** — mobile-first
- **Fuentes:** Configurable en `src/styles/global.css`

## 🌍 Internacionalización

```javascript
// Cambiar idioma sin recargar página
import { useTranslation } from 'react-i18next';
const { t, i18n } = useTranslation();
i18n.changeLanguage('es'); // o 'en'
```

## 📦 Secciones disponibles out-of-the-box

- Hero con CTA
- About / Misión
- Mission statement
- Product/Feature showcase
- Testimonials
- Contact form (funcional)
- Footer

## ⚡ Deploy a GitHub Pages

```bash
npm install gh-pages --save-dev
# En package.json agregar:
# "homepage": "https://tuuser.github.io/tu-repo"
# "predeploy": "npm run build"
# "deploy": "gh-pages -d build"
npm run deploy
```
