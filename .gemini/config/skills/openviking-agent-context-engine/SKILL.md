---
name: openviking-agent-context-engine
description: Gestión jerárquica de contexto L0/L1/L2, memoria a largo plazo para agentes y Context File System con protocolo viking:// basado en Volcengine OpenViking.
---

# Skill: OpenViking Agent Context Engine

## Propósito
Implementar un sistema de contexto estructurado ("Context File System") para agentes de IA que organiza la memoria, el conocimiento RAG y la identidad del agente mediante un sistema de archivos virtual (`viking://`), optimizando el consumo de tokens mediante cargas por niveles (L0/L1/L2).

## Arquitectura de Contexto Jerárquico
1. **Compresión de Tokens en 3 Niveles:**
   - **L0 (Abstract):** Resumen ultra-compacto para selección rápida de contexto.
   - **L1 (Overview):** Estructura detallada y mapa de relaciones.
   - **L2 (Detail):** Contenido bruto/código fuente cargado bajo demanda.
2. **Navegación de Contexto (Context File System):**
   - Agentes pueden explorar su propia memoria utilizando operaciones `ls`, `tree` y `find` sobre rutas `viking://`.
3. **Memoria de Sesión a Largo Plazo:**
   - Extracción de preferencias del usuario, entidades y patrones entre sesiones de interacción.
