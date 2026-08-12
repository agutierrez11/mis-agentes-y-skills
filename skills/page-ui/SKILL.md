---
name: page-ui
description: >
  Colección de componentes y templates de landing page para React y Next.js,
  construidos con TailwindCSS. Open source, copy-paste, temeable.
  Úsalo cuando necesites componentes de landing page de alta conversión:
  hero, features, pricing, testimonials, CTA, FAQ. Sin modo oscuro neón.
  Repo: https://github.com/PageAI-Pro/page-ui | Docs: https://pageui.dev
---

# Page UI — Landing Page Components for React & Next.js

**Repo:** https://github.com/PageAI-Pro/page-ui  
**Docs:** https://pageui.dev  
**Stack:** Next.js + TailwindCSS v3 + shadcn/ui  
**Modelo:** Copy-paste components (como shadcn, no es una dependencia npm)

---

## Cuándo usar esta Skill

- Usuario quiere componentes de landing page de alta conversión
- Necesita hero, pricing, testimonials, FAQ, features en Next.js
- Quiere copy-paste rápido sin instalar librerías pesadas
- Diseño limpio, no de AI/neón

---

## 🚀 Instalación

```bash
# 1. Crear proyecto Next.js con Tailwind
npx create-next-app@latest my-app --typescript --tailwind --eslint

# 2. Init Page UI CLI
npx @page-ui/wizard@latest init

# 3. Dependencias necesarias
npm install @tailwindcss/forms @tailwindcss/typography tailwindcss-animate \
  class-variance-authority clsx tailwind-merge lucide-react \
  @radix-ui/react-accordion
```

## 🎨 Variables CSS base (en `global.css`)

```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 240 10% 3.9%;
    --card: 0 0% 100%;
    --card-foreground: 240 10% 3.9%;
    --primary: 346.8 77.2% 49.8%;
    --primary-foreground: 355.7 100% 97.3%;
    --secondary: 240 4.8% 95.9%;
    --muted: 240 4.8% 95.9%;
    --muted-foreground: 240 3.8% 46.1%;
    --border: 240 5.9% 90%;
    --radius: 0.5rem;
  }
}
```

## 📦 Componentes Disponibles (Copy-Paste)

### Hero Section
```tsx
import { LandingHero } from '@/components/landing/LandingHero';

<LandingHero
  title="Tu Producto"
  description="Una línea que convierte"
  ctaText="Empieza Gratis"
  ctaHref="/signup"
/>
```

### Features Grid
```tsx
import { LandingProductFeatures } from '@/components/landing/LandingProductFeatures';

const features = [
  { title: "Rápido", description: "...", icon: <Zap /> },
  { title: "Seguro", description: "...", icon: <Shield /> },
];

<LandingProductFeatures features={features} />
```

### Pricing Cards
```tsx
import { LandingPricing } from '@/components/landing/LandingPricing';

<LandingPricing
  plans={[
    { name: "Free", price: "$0", features: ["Feature 1"] },
    { name: "Pro", price: "$29/mo", features: ["Feature 1", "Feature 2"], highlighted: true },
  ]}
/>
```

### Testimonials
```tsx
<LandingTestimonials
  testimonials={[
    { quote: "Increíble producto.", name: "María García", role: "CEO @ Startup" },
  ]}
/>
```

## 🏗️ Templates disponibles

| Template | Caso de uso |
|----------|-------------|
| **Specta** | Plataforma de creadores |
| **Gnomie AI** | SaaS B2C con carrusel |
| **Minimum Via** | Producto minimalista |
| **ScreenshotTwo** | Developer tool |

Ver todos en: https://shipixen.com/demo/landing-page-templates

## ⚡ Deploy

```bash
# Vercel (recomendado para Next.js)
vercel deploy --prod

# GitHub Pages (solo si es export estático)
next build && next export
```

## ⚠️ Restricción importante

- Funciona con **Tailwind v3** solamente
- Tailwind v4 no soportado aún (2025)
