---
name: clean-light-ui
description: >
  Diseña interfaces web con estética light mode limpia (shadcn/Linear/Notion).
  Sin modo oscuro, sin neones, sin glassmorphism. Fondo blanco, tipografía Inter,
  bordes sutiles, grid de tarjetas con tags de estado en pasteles.
  Usa cuando el usuario quiera una UI web profesional que NO parezca un producto de AI.
---

# Clean Light UI — Sistema de Diseño Minimalista

## Cuándo usar esta Skill

Actívala cuando el usuario pida:
- "Quita el modo oscuro"
- "No quiero neones ni gradientes"
- "Algo más limpio, profesional"
- "Como Notion / Linear / shadcn"
- Rediseñar cualquier HTML que tenga `background: #0a0a0a` o paletas púrpura/cyan neón

## Filosofía de Diseño

**Inspiración:** shadcn/ui · Linear · Notion · Stripe Docs  
**Anti-patrones a eliminar:** glassmorphism · fondos oscuros · gradientes neón · sombras de glow · `backdrop-filter: blur`

---

## 🎨 Design Tokens Canónicos

```css
:root {
  --white:   #ffffff;
  --bg:      #f9fafb;   /* fondo de página */
  --border:  #e5e7eb;   /* bordes de cards */
  --muted:   #6b7280;   /* texto secundario */
  --text:    #111827;   /* texto principal */
  --text-2:  #374151;   /* texto de cuerpo */
  --primary: #2563eb;   /* único acento (azul) */
  --primary-light: #eff6ff;
  --radius:  10px;
  --shadow:  0 1px 3px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.04);
  --shadow-lg: 0 4px 24px rgba(0,0,0,.08);
}
```

## 🔤 Tipografía

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

- **Cuerpo:** `Inter` — letter-spacing: -0.01em en títulos
- **Código/números:** `JetBrains Mono`
- **NUNCA usar:** Outfit con colores neón, ninguna fuente con `text-shadow` de glow

## 🃏 Patrón de Card

```html
<a href="..." class="card">
  <div class="card-icon-wrap">🎯</div>
  <div class="card-header">
    <div>
      <div class="card-num">Módulo 01</div>   <!-- JetBrains Mono 0.65rem muted -->
      <div class="card-title">Título</div>
    </div>
    <span class="card-arrow">↗</span>
  </div>
  <p class="card-desc">Descripción del módulo.</p>
  <div class="card-footer">
    <span class="card-tag blue">Etiqueta</span>
  </div>
</a>
```

### Tags de Estado (pasteles, no neón):

| Clase | Color texto | Background | Border |
|-------|-------------|------------|--------|
| `.card-tag.green`  | `#15803d` | `#f0fdf4` | `#bbf7d0` |
| `.card-tag.blue`   | `#1d4ed8` | `#eff6ff` | `#bfdbfe` |
| `.card-tag.amber`  | `#b45309` | `#fffbeb` | `#fde68a` |
| `.card-tag.red`    | `#b91c1c` | `#fef2f2` | `#fecaca` |
| `.card-tag.purple` | `#7c3aed` | `#f5f3ff` | `#ddd6fe` |
| `.card-tag.pink`   | `#be185d` | `#fdf2f8` | `#fbcfe8` |

## 📐 Layout

```css
/* Grid de cards */
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  padding: 0 40px 80px;
}

/* Card featured (span 2 cols) para destacar el módulo principal */
.card.featured { grid-column: span 2; flex-direction: row; }

/* Header sticky blanco con borde */
header {
  background: #fff;
  border-bottom: 1px solid #e5e7eb;
  position: sticky; top: 0;
  height: 60px;
}
```

## ✅ Checklist antes de entregar

- [ ] `background` de body es `#f9fafb` o `#ffffff`
- [ ] Cero `background: #0` o `hsl(220 ...) dark`
- [ ] Cero `box-shadow: 0 0 20px rgba(99,102,241` (glow)
- [ ] Fuente es `Inter`, no `Outfit` con gradientes
- [ ] Tags de estado son pasteles, no solid neón
- [ ] Header blanco con `border-bottom: 1px solid #e5e7eb`
- [ ] Footer minimalista blanco con pills de texto muted
