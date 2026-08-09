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

## 🎨 Biblioteca de Prompts (`pen.dev/prompts`)
- **Payment Checkouts & Dashboards:** Generación de flujos de pago B2B, terminales virtuales, cotizadores y conciliación bancaria.
- **Landing Pages & B2B Portals:** Maquetación rápida de plataformas corporativas con estética de alta gama (Dark Mode, Glassmorphism, Bento Grid).
