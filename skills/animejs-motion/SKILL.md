---
name: animejs-motion
description: Guía de animación e integración de anime.js (juliangarnier/anime) para micro-interacciones fluidas, tickers de números en vivo, animación de grafos SVG y staggers en interfaces web.
---

# anime.js Motion Engine: Animaciones Fluidas y Micro-Interacciones

## Descripción
`anime.js` (Julian Garnier) es un motor de animación JavaScript ultraligero (~14KB) diseñado para manipular propiedades CSS, SVG paths, atributos del DOM, objetos JS y curvas de tiempo (*easing*) con aceleración por GPU sin afectar el rendimiento.

---

## 1. Importación e Instalación

### Vía CDN (Vanilla HTML / Single File Apps)
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.2/anime.min.js"></script>
```

### Vía npm / ES Modules (Vite, Next.js, React)
```bash
npm install animejs
```
```javascript
import anime from 'animejs/lib/anime.es.js';
```

---

## 2. Patrones de Animación Clave

### A. Ticker de Números en Vivo (Count-Up / Count-Down para Fichas KPI)
Ideal para animar contadores numéricos (ej. de `3039` a `3022`) cuando se filtran o purgan contactos en dashboards comerciales.

```javascript
function animateKpiNumber(elementId, startVal, endVal, duration = 600) {
  const obj = { val: startVal };
  const el = document.getElementById(elementId);
  if (!el) return;

  anime({
    targets: obj,
    val: endVal,
    round: 1,
    easing: 'easeOutExpo',
    duration: duration,
    update: function() {
      el.textContent = obj.val.toLocaleString();
    }
  });
}
```

---

### B. Animación por Cascadas (*Staggering*) en Tablas y Grids
Entrada o actualización secuencial de filas de tablas o tarjetas Kanban.

```javascript
// Revelar tarjetas o filas con retardo escalonado de 30ms
anime({
  targets: '.compact-table tbody tr',
  opacity: [0, 1],
  translateY: [12, 0],
  delay: anime.stagger(30), // 30ms de retardo entre cada fila
  easing: 'easeOutCubic',
  duration: 400
});
```

---

### C. Salida Suave al Descartar/Eliminar Elementos
Animación de salida antes de remover una tarjeta o fila del DOM.

```javascript
function removeElementSmoothly(element, onComplete) {
  anime({
    targets: element,
    opacity: [1, 0],
    translateX: [0, -30],
    scale: [1, 0.95],
    easing: 'easeOutQuad',
    duration: 250,
    complete: function() {
      if (onComplete) onComplete();
    }
  });
}
```

---

### D. Animación de Grafos de Red y SVG Paths (Dibujo de Conexiones B2B)
Animar líneas de trazado en diagramas o nodos de relación de contactos.

```javascript
anime({
  targets: 'path.network-link',
  strokeDashoffset: [anime.setDashoffset, 0],
  easing: 'easeInOutSine',
  duration: 1200,
  delay: function(el, i) { return i * 100; }
});
```

---

### E. Micro-interacciones de Botones y Badges (Pulse & Glow)
Resplandor sutil o pulso al cambiar estados (ej. de *Sin verificar* a *✨ Verificado Live*).

```javascript
function pulseBadge(badgeElement) {
  anime({
    targets: badgeElement,
    scale: [1, 1.15, 1],
    boxShadow: [
      '0 0 0px rgba(16, 185, 129, 0)',
      '0 0 12px rgba(16, 185, 129, 0.6)',
      '0 0 0px rgba(16, 185, 129, 0)'
    ],
    easing: 'easeOutElastic(1, .5)',
    duration: 600
  });
}
```

---

## 3. Principios de Diseño y Rendimiento

1. **Priorizar `transform` y `opacity`:** Evita animar propiedades como `top`, `left`, `margin` o `width` directamente para no forzar *layout reflows* en el navegador. Usa `translateX`, `translateY`, `scale` y `opacity`.
2. **Duraciones Pragmáticas (200ms - 500ms):** Las animaciones UI deben ser rápidas e imperceptibles al trabajo operativo. 200ms-350ms es el estándar para respuestas de clic.
3. **Easing Recomendados:**
   - Movimientos UI generales: `easeOutCubic` o `easeOutQuad`.
   - Números/KPIs: `easeOutExpo`.
   - Pulso o badges: `easeOutElastic(1, .6)`.
