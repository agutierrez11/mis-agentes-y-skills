---
name: awesome-claude-design
description: Cat?logo y framework de 68 sistemas de dise?o listos para producci?n para agentes de IA (DESIGN.md, tokens HSL curados, tipograf?as Google Fonts, Bento Grids, micro-animaciones, glassmorphism y est?ticas inspiradas en Linear, Stripe, Vercel, Apple, Supabase y m?s).
---

# ?? Awesome Claude Design ? Design System Framework

Gu?a operativa para construir interfaces de usuario de nivel mundial con est?tica de alta gama (Linear, Stripe, Vercel, Supabase, Apple) mediante archivos `DESIGN.md` y tokens de dise?o estructurados.

---

## ?? Principios Rectores de Dise?o
1. **Zero Placeholders:** Nunca usar im?genes grises ni textos `Lorem Ipsum`. Todo contenido debe tener data dura, cifras de negocio reales y recursos gr?ficos generados.
2. **Tema Oscuro & Contrastes HSL:** Colores de fondo profundos (`#0A0F1D`, `#0B132B`), bordes sutiles con opacidades calculadas (`rgba(255,255,255,0.08)`), y acentos vibrantes (Teal `#5EEAD4`, Emerald `#10B981`, Rose `#F43F5E`, Indigo `#6366F1`).
3. **Tipograf?a Jer?rquica:** 
   - T?tulos y N?meros KPI: *Outfit*, *Inter* o *Plus Jakarta Sans*.
   - Datos monetarios, tickers y tags t?cnicos: *JetBrains Mono* o *Space Mono*.
4. **Micro-interacciones y Animaciones de F?sica:** Transiciones con `cubic-bezier(0.16, 1, 0.3, 1)`, efectos hover de elevaci?n (`translateY(-2px)`), glow reactivo y tooltips instant?neos.

---

## ??? Estilos y Familias de Dise?o Disponibles
- **Linear-Dark:** Minimalismo t?cnico, grids oscuros, bordes de 1px con degradados de luz y atajos de teclado visibles.
- **Stripe-Fintech:** Gradientes aurora vibrantes, tipograf?a corporativa premium y micro-gr?ficos interactivos.
- **Vercel-Geist:** Monocrom?tico de alto contraste, tipograf?a densa y transiciones instant?neas.
- **Bento Grid Executive:** Mosaico modular de tarjetas interconectadas con densidades variables.
- **Glassmorphism Pro:** Desenfoques de fondo (`backdrop-filter: blur(12px)`), bordes transl?cidos y capas flotantes.

---

## ??? C?mo Usar en Agentes
1. Seleccionar la familia de dise?o adecuada seg?n el tipo de producto (FinTech, B2B SaaS, Analytics Dashboard, Pitch Deck).
2. Declarar las variables CSS en `:root` con valores HSL/HEX armonizados.
3. Asegurar que cada componente tenga estados interactivos (`:hover`, `:active`, `:focus-visible`).
