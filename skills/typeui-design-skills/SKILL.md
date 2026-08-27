---
name: typeui-design-skills
description: Generación e integración de más de 90 estilos de diseño UI/UX (Glassmorphism, Bento Grid, Neumorphism, Minimalist, Industrial Brutalism) para maquetas y aplicaciones web usando TypeUI.
---

# 🎨 TypeUI Design Skills — Estilos de Diseño UI/UX para Agentes

Esta habilidad proporciona patrones y reglas de diseño visual de alta fidelidad extraídos de **TypeUI** (`typeui.sh`). Se utiliza para forzar a la IA a generar código frontend (React, TailwindCSS, Vanilla CSS) con estética impecable nivel Vercel, Stripe o Linear.

## 🛠️ Comandos CLI
Para descargar o actualizar estilos de diseño específicos de la galería oficial de TypeUI:

```bash
# Descargar un estilo de diseño específico (ej. glassmorphism, bento, minimalist)
npx typeui.sh pull glassmorphism

# Generar un SKILL.md personalizado de diseño a partir de tu sistema de diseño actual
npx typeui.sh generate

# Actualizar las habilidades de diseño instaladas
npx typeui.sh update
```

## 📐 Estilos Principales Soportados
1. **Glassmorphism:** Efectos de desenfoque de fondo (`backdrop-blur-md`), bordes semitransparentes (`border-white/10`) y gradientes oscuros sutiles.
2. **Bento Grid:** Retículas planas estructuradas tipo Bento con tarjetas con bordes redondeados (`rounded-2xl`), sombras suaves e íconos contrastantes.
3. **Industrial Brutalism:** Tipografía en negrita (`font-mono`, `uppercase`), contrastes fuertes, bordes marcados (`border-2 border-black`), cero gradientes y estructura cruda.
4. **Editorial Minimalist:** Paletas monocromáticas cálidas, tipografía elegante (Outfit, Serif/JetBrains Mono), contrastes tipográficos y micro-animaciones suaves.

## 🎯 Reglas de Aplicación
- **Cero Placeholders:** Siempre usar contenido o datos reales de la industria. Si se requiere una imagen, generarla con la herramienta de imágenes.
- **Tipografía Google Fonts:** Priorizar fuentes de alta gama como Inter, Outfit, Roboto o JetBrains Mono.
- **Diseño Responsive:** Layouts 100% adaptables con CSS Grid y Flexbox sin desbordamientos horizontales.
