---
name: khoj-second-brain
description: Configuración, búsqueda semántica y consultas RAG locales con Khoj (khoj-ai/khoj), el "Segundo Cerebro" con IA para indexar documentos, PDFs y notas privadas.
---

# 🧠 Khoj — AI Second Brain & Personal RAG Engine

Esta habilidad le permite a Antigravity interactuar con **Khoj** (`github.com/khoj-ai/khoj`), una plataforma Open-Source de "Segundo Cerebro" con RAG (Retrieval-Augmented Generation) para buscar e indexar conocimiento personal y documentos locales.

## 🛠️ Comandos de Despliegue e Instalación
```bash
# Instalación rápida con Docker
docker run -d -p 42110:42110 khojai/khoj:latest

# O instalación mediante Python/pip
pip install khoj
khoj
```

## 📁 Fuentes de Datos Soportadas
- **Documentos Locales:** Archivos `.pdf`, `.md`, `.docx`, `.org`
- **Integraciones:** Bóvedas de Obsidian, Emacs, Notion, GitHub Repositories.
- **Modelos LLM:** Soporta modelos locales (vía Ollama/Llama.cpp) y APIs en la nube (Claude, OpenAI, Gemini).

## 🎯 Caso de Uso en Antigravity
- **Búsqueda Semántica:** Consultar datos auditados de comisiones, métricas de Clip/Fiserv o contratos archivados sin realizar búsquedas manuales de texto plano.
- **Respuestas con Citas:** Extraer párrafos exactos con sus rutas de archivo fuente para respaldar propuestas ejecutivas.
