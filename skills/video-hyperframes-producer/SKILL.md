---
name: video-hyperframes-producer
description: Diseña y produce videos MP4 deterministas de alta calidad para presentaciones B2B, intros de producto, gráficos de datos y demos comerciales usando HTML, CSS, SVG y el motor HyperFrames.
---

# 🎬 Video & Motion Graphics Producer (HyperFrames)

Esta skill enseña al agente de IA a planificar, maquetar y renderizar videos MP4 profesionales para presentaciones ejecutivas, intros de producto, dashboards en movimiento y demostraciones B2B utilizando HTML, CSS, SVG y la arquitectura de animación basada en tiempo de HyperFrames.

---

## 🚀 1. Principios de Animación y Maquetación de Video HTML

A diferencia de los videos tradicionales basados en fotogramas clave por software de edición (After Effects/Premiere), HyperFrames renderiza HTML y CSS cuadro por cuadro de forma **determinista**.

### Reglas Clave de Diseño:
* **Resolución Estándar:** 1920x1080 (16:9 HD) o 1080x1920 (9:16 Vertical para Reels/LinkedIn).
* **Duración y Timeline:** Cada escena se define mediante atributos de tiempo explícitos (`data-duration`, `data-timeline-start`).
* **Estética Premium:**
  * Uso de paletas oscuras tailoreadas (`#0F172A`, `#090D16`, `#1E1B4B`).
  * Gradientes líquidos, brillos (`backdrop-filter: blur()`), tipografías modernas (Google Fonts: Outfit, JetBrains Mono, Inter).
  * Tipografías con tamaño relativo escalado para lectura clara en pantalla.

---

## 🛠️ 2. Estructura de Escenas y Componentes

### 1. Intro & Título del Producto (0s - 3s)
* Animación de entrada de logo/marca con `opacity: 0` a `1` y `transform: scale(0.95)` a `scale(1)`.
* Tipografía limpia con brillo metálico o gradiente en texto (`background-clip: text`).

### 2. Demostración de Métricas / Data Visualization (3s - 7s)
* Gráficas animadas en SVG o barras de datos con `width` animado según tiempo transcurrido.
* Tarjetas de KPIs estilo dashboard en vivo con contadores de números en tiempo real.

### 3. Cierre y Llamado a la Acción (7s - 10s)
* Contacto ejecutivo, URL de aterrizaje y logo final.
* Transición suave de salida (`fade-out`).

---

## ⚡ 3. Flujo de Producción Autónoma con Agentes

Cuando el usuario pida un video promocional, intro de producto o gráfica animada:
1. **Planificar el Storyboard:** Definir duración total, número de escenas y mensaje clave.
2. **Generar el HTML/CSS de la composición:** Crear los contenedores de escena y las animaciones sincronizadas en tiempo.
3. **Validar y Renderizar:** Utilizar los scripts de renderizado o Puppeteer/FFmpeg para generar el archivo de video final en `.mp4`.
