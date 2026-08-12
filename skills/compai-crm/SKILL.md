---
name: compai-crm
description: Operación, despliegue y gestión del CRM Open-Source agéntico CompAI (trycompai/crm) para prospección autónoma, pipelines y actualización de leads mediante agentes de IA.
---

# 💼 CompAI — Agentic-First CRM Platform

Esta habilidad permite desplegar, consultar y sincronizar datos dentro de **CompAI** (`github.com/trycompai/crm`), el primer CRM código abierto diseñado para ser operado autónomamente por agentes de IA.

## 🚀 Arquitectura y Stack
- **Frontend:** Next.js (TypeScript) + TailwindCSS
- **Backend:** NestJS + Prisma ORM
- **Base de Datos:** PostgreSQL
- **Ejecución:** Docker Compose + Bun runtime

## 🛠️ Comandos de Despliegue Local (Docker)
```bash
# Clonar repositorio de CompAI
git clone https://github.com/trycompai/crm.git
cd crm

# Levantar infraestructura con Docker
docker compose up -d
```

## 🎯 Protocolos para el Agente Comercial
1. **Calificación Autónoma de Leads:** Leer registros entrantes, consultar enriquecimiento de datos de la empresa y asignar scoring de ICP (Ideal Customer Profile).
2. **Actualización de Pipeline:** Mover cuentas entre etapas (Prospección -> Discovery -> Demo -> Propuesta -> Cerrado/Ganado) de acuerdo con los registros de conversación.
3. **Registro de Interacciones:** Registrar cada nota de llamada, correo enviado o interacción de WhatsApp directamente en las tablas de Prisma sin intervención manual del usuario.
