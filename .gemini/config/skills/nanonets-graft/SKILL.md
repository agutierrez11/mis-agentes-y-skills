---
name: nanonets-graft
description: Graft Context Engine por NanoNets. Mapeo de código por grafo mediante Tree-Sitter para mantener a los agentes sincronizados sin romper dependencias en Git.
---

# NanoNets Graft: Motor de Contexto de Código en Git

## Descripción
Graft (`NanoNets/Graft`) es un motor de contexto de código de código abierto que construye un grafo del repositorio usando `tree-sitter`, persistiendo el conocimiento del proyecto en archivos markdown vinculados dentro del mismo control de versiones.

## Características
1. **Tree-Sitter Structural Analysis:** Análisis estructural rápido de símbolos sin requerir claves de API.
2. **Persistencia en Git:** Comparte el contexto del mapa de código con todo el equipo y subagentes.
3. **Compatibilidad:** Se integra como servidor MCP (Model Context Protocol) o hooks para agentes de IA (Claude Code, Gemini, Cursor).

## Instalación y Uso
```bash
npm install -g @nanonets/graft
graft init
```
