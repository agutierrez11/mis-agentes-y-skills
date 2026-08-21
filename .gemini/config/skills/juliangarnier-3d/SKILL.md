---
name: juliangarnier-3d
description: Guía de integración de maquetas 3D interactivas, visualizadores 3D de libros y reportes (juliangarnier/3D-book-preview), y micro-efectos de física/hover estilo Julian Garnier para pitch decks B2B y lead magnets.
---

# Julian Garnier 3D & Interactive Motion Engine

## Descripción
Esta skill proporciona los patrones de diseño e ingeniería visual creados por **Julian Garnier** para maquetas 3D interactiva en CSS/JS (libros, dossiers comerciales, reportes en 3D), rotación guiada por cursor (*cursor-following 3D tilt*), y tarjetas con reflejo dinámico (*glassmorphism shimmer*).

---

## 1. Visualizador 3D de Libros y Whitepapers (3D Book Preview)

Ideal para presentar Lead Magnets B2B, Bóvedas de Ventas Socráticas o Reportes de Eficiencia Transaccional en landing pages y modales comerciales.

### Estructura HTML (Minimalista & Autónoma)

```html
<div class="book-container">
  <div class="book" id="interactive-book">
    <!-- Portada -->
    <div class="book-cover">
      <div class="book-cover-front">
        <div class="book-title">CPS OS: Guía Socrática B2B</div>
        <div class="book-author">Antonio Gutiérrez</div>
      </div>
      <div class="book-cover-back"></div>
    </div>
    <!-- Lomo -->
    <div class="book-spine">
      <span>CPS SOCRATIC GUIDE</span>
    </div>
    <!-- Páginas interiores -->
    <div class="book-pages"></div>
  </div>
</div>
```

### Estilo CSS 3D (Preservación de Perspectiva)

```css
.book-container {
  perspective: 1200px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
}

.book {
  position: relative;
  width: 220px;
  height: 320px;
  transform-style: preserve-3d;
  transform: rotateY(-25deg) rotateX(10deg);
  transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
  cursor: pointer;
}

.book:hover {
  transform: rotateY(-5deg) rotateX(0deg) scale(1.05);
}

.book-cover-front {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #1f2328 0%, #0d1117 100%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 4px 8px 8px 4px;
  box-shadow: 15px 15px 30px rgba(0, 0, 0, 0.4);
  padding: 24px;
  color: #f0f6fc;
}

.book-spine {
  position: absolute;
  left: -20px;
  width: 20px;
  height: 100%;
  background: #161b22;
  transform: rotateY(-90deg);
  transform-origin: right;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #8b949e;
  font-size: 10px;
  letter-spacing: 2px;
}
```

---

## 2. Micro-Interacción: 3D Tilt Siguiendo el Cursor

Efecto de inclinación interactiva en 3D para tarjetas de propuesta, calculadoras de COI y componentes UI de alto estatus.

```javascript
function applyJulian3DTilt(cardElement) {
  if (!cardElement) return;

  cardElement.addEventListener('mousemove', (e) => {
    const rect = cardElement.getBoundingClientRect();
    const x = e.clientX - rect.left; // Posición X dentro de la tarjeta
    const y = e.clientY - rect.top;  // Posición Y dentro de la tarjeta
    
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    
    const rotateX = ((y - centerY) / centerY) * -12; // Máximo 12deg
    const rotateY = ((x - centerX) / centerX) * 12;

    cardElement.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
  });

  cardElement.addEventListener('mouseleave', () => {
    cardElement.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
    cardElement.style.transition = 'transform 0.5s ease';
  });
}
```

---

## 3. Integración con Anime.js para Morphing de Rutas SVG

Para animar esquemas de arquitectura de pagos (POS -> Switch -> Adquirente -> Banco Emisor):

```javascript
import anime from 'animejs';

// Morfosis entre dos estados de un flujo transaccional SVG
function animateTransactionFlow(svgPathElement, newPathData) {
  anime({
    targets: svgPathElement,
    d: [
      { value: newPathData }
    ],
    easing: 'easeOutElastic(1, .8)',
    duration: 1200
  });
}
```

---

## 💡 Reglas de Diseño de Julian Garnier
1. **Zero Layout Thrashing:** Usar siempre `transform` y `opacity` acelerados por GPU.
2. **Easing Natural:** Curvas de salida largas (`easeOutExpo`, `cubic-bezier(0.2, 0.8, 0.2, 1)`) para simular peso físico real.
3. **Perspectiva Controlada:** Mantener `perspective: 1000px` a `1200px` para evitar distorsiones ópticas agresivas.
