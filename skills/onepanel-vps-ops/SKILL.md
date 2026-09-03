---
name: onepanel-vps-ops
description: Administración, despliegue y gestión de servidores Linux y cargas de trabajo agénticas con 1Panel (1Panel-dev/1Panel), el panel de control open-source Metal-to-Agent con AI Gateway, Docker y Skills Hub.
---

# 🎛️ 1Panel VPS & Agentic Ops Skill

Esta skill proporciona las directrices y mejores prácticas para instalar, administrar y orquestar servidores Linux (VPS como Contabo, OVHcloud, Hetzner) utilizando **1Panel** (`1Panel-dev/1Panel`), la plataforma de gestión *Metal-to-Agent*.

---

## 🎯 Capacidades Clave de 1Panel

1. **Gestión Metal-to-Agent:** Control unificado de la infraestructura física/VPS hasta los contenedores y agentes de IA.
2. **AI Gateway Integrado:** Proxy centralizado de modelos LLM con balanceo de carga, control de cuotas y auto-fallback.
3. **Skills Hub:** Repositorio centralizado para distribuir e instalar herramientas agénticas en los servidores de producción.
4. **Orquestación Docker & App Store:** Instalación en 1-clic de bases de datos (PostgreSQL, Redis), Nginx, Supabase, n8n y entornos en Python/FastAPI.

---

## 🚀 Despliegue Rápido en VPS (Contabo / Ubuntu / Debian)

### 1. Comando de Instalación Oficial (Linux)

```bash
curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sudo bash quick_start.sh
```

### 2. Configuración de Seguridad Recomendada
* **Puerto Personalizado:** Cambiar el puerto por defecto de administración (`8888`) por uno aleatorio (ej. `39420`).
* **WAF & SSL:** Activar Let's Encrypt SSL automático para la interfaz de administración y las APIs expuestas.
* **Firewall (UFW):** Restringir el acceso al panel solo a direcciones IP permitidas o VPN.

---

## 🐳 Arquitectura de Contenedores para Radar Comercial en 1Panel

```text
[ 1Panel Reverse Proxy / Nginx ]
        │
        ├──> FastAPI Backend (Docker: Python 3.11 / Uvicorn)
        ├──> Redis Cache (Docker: Procesamiento de Colas Harvest/Apify)
        ├──> Supabase Self-Hosted / PostgreSQL 16 (Base de datos relacional)
        └──> AI Gateway (1Panel: Enrutamiento de Gemini / Qwen / Anthropic)
```

---

## 📋 Checklist de Mantenimiento y Respaldos

- [ ] **Backups Automáticos:** Programar backups diarios de volumenes Docker y bases de datos a S3 o almacenamiento externo.
- [ ] **Monitoreo de Recursos:** Alertas de consumo de RAM/CPU en el VPS de Contabo.
- [ ] **Actualización de 1Panel:** Mantener el panel en la versión estable más reciente directamente desde la interfaz web.
