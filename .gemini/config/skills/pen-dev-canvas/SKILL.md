---
name: pen-dev-canvas
description: Diseño visual de interfaces y maquetas interactivas en el IDE con Pen.dev (pencil.dev), archivos .pen nativos de Git, prompts de UI y protocolo MCP.
---

# ✏️ Pen.dev — AI-Driven In-IDE Design Canvas

Esta habilidad le permite a Antigravity interactuar con **Pen.dev** (`pen.dev`), el lienzo de diseño de interfaces impulsado por IA que vive directamente dentro del IDE y versiona las maquetas en archivos `.pen` nativos de Git.

## 🚀 Conceptos Core
1. **Lienzo en el IDE:** Diseñar componentes y pantallas visuales sin salir del editor de código (sustituto ágil de Figma para desarrolladores).
2. **Archivos `.pen` Git-Natives:** Los diseños se guardan en formato JSON dentro del repositorio y se versionan con `git commit` y `git push`.
3. **Model Context Protocol (MCP) & CLI:** El agente de IA puede leer el lienzo, generar interfaces completas a partir de prompts y exportar directamente a React, TailwindCSS y HTML.

## 🛠️ Comandos CLI
```bash
# Instalar o ejecutar Pen.dev CLI
npx @pen.dev/cli

# Iniciar el lienzo interactivo
npx @pen.dev/cli start
```

## 🎨 Biblioteca de Prompts Oficiales (`pen.dev/prompts`)

### 1. Generación Inicial de Interfaces
* **Web App Técnico:** `Design a web app for managing rocket launches. Use a technical style.`
* **Sitio Web de Marca:** `Design a website for a specialty cafe in Haight Ashbury, San Francisco.`
* **App Móvil Minimalista:** `Design a mobile app for tracking music royalties. Use a Scandinavian minimalistic style.`

### 2. Iteración y Evolución de Diseño
* **Ajustar Código al Diseño:** `Look at the selected design. Adjust the prompts page code to reflect it. You can find the images in the /public folder. Don't worry about header and footer, keep it as it is on the current page.`
* **Crear Nueva Página / Módulo:** `Use the selected design as the base design, that's my current app. Design a new page, the Missions page now. Create a new design for it.`
* **Explorar Dirección Opuesta:** `Look at the selected design. Explore a totally different design direction.`
* **Cambiar Layout manteniendo Estilo:** `Look at the selected design. Explore a different layout, but keep the current design direction. Create a new design for it.`
* **Cambio de Tema (Light / Dark Mode):** `Look at the selected design. Change it to the light mode. Create a new design for it.`
* **Estilo Suizo / Tipográfico:** `Let's go more bold and rock'n'roll, make the headline much larger, drop boxes around prompts and just focus on typography, one column layout, most emphasis on prompts, everything else secondary, Swiss layout.`
* **Cambio de Tipografía:** `That's great. Now change fonts to something more classy. Create a new design for it.`
* **Cambio Estructural de Navegación:** `Great! Now use a sidenav. Create a new design for it.`
* **Simplificación y Limpieza:** `Look at the selected design. Change this to a simpler and cleaner design direction. Create a new design for it.`
