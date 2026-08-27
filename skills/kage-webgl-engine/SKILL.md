---
name: kage-webgl-engine
description: Motor de mundos y experiencias 3D interactivas guiadas por scroll (Scroll Worlds Engine) en Three.js/WebGL en un solo archivo HTML aut?nomo (~1MB sin dependencias de red en runtime).
---

# ?? Kage WebGL Engine ? 3D Scroll Worlds

Arquitectura para la creaci?n de experiencias web inmersivas en 3D aut?nomas contenidas en un ?nico archivo HTML.

---

## ?? Componentes del Motor
1. **Single-File Architecture:** Canvas Three.js, shaders GLSL, geometr?as y l?gica de renderizado embebidas sin dependencias externas pesadas.
2. **Scroll-Driven Camera:** Interpolaci?n suave de c?mara y foco (`lerp`, `damp`) vinculada al progreso del scroll del usuario.
3. **Sistemas de Part?culas y Clima:** Emisores din?micos de part?culas (polvo de luz, niebla volum?trica, hojas/chispas) con aceleraci?n GPU.
4. **Iluminaci?n Reactiva:** Luces puntuales y ambientales que var?an seg?n la secci?n o interacci?n del cursor.

---

## ?? Aplicaci?n en Landings FinTech y Tur?sticas
- Visualizaci?n interactiva del flujo de transacciones cruzando continentes hacia terminales en el Caribe.
- Tarjetas hologr?ficas en 3D que rotan al interactuar con el mouse.
- Optimizaci?n de rendimiento a 60 FPS con bajo consumo de CPU/GPU en dispositivos m?viles.
