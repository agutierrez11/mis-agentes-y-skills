---
name: opensandbox
description: Ejecución segura de código, sandboxing de grado de producción, automatización de navegadores (Playwright/Chrome) y entornos microVM/Docker/K8s para agentes usando OpenSandbox (opensandbox-group/OpenSandbox).
---

# 🛡️ OpenSandbox — Production-Grade Agent Execution Sandbox

Esta habilidad guía el uso y despliegue de **OpenSandbox** (`opensandbox-group/OpenSandbox`) para proporcionar entornos de ejecución seguros, aislados y controlados para agentes de IA.

## 🔑 Pilares de Aislamiento y Seguridad
1. **Aislamiento Multi-Nivel:**
   - **Contenedores Ligeros:** Docker para desarrollo y pruebas rápidas.
   - **Aislamiento Seguro:** Soporte para gVisor, Kata Containers y microVMs Firecracker para aislar código no confiable.
2. **Entornos de Automatización Integrados:**
   - **Browser Sandboxes:** Sesiones aisladas de Chrome y Playwright para web scraping, testing de UIs y navegación web autónoma.
   - **Desktop GUI Environments:** Entornos interactivos con VNC / VS Code para tareas de desarrollo complejas.
3. **Control de Red y Credenciales:**
   - Bóveda de credenciales (*Credential Vault*) para inyección segura de API keys.
   - Políticas de red con control de tráfico de salida (*egress control*) para evitar exfiltración de datos.

## 🛠️ Modos de Operación
* **CLI `osb`:** Gestión de ciclo de vida de sandboxes desde la terminal.
* **Unified Sandbox Protocol:** API unificada para crear, ejecutar comandos, transferir archivos y destruir sandboxes programáticamente desde SDKs de Python o Node.js.
* **Orquestación en Producción:** Despliegue sobre clústeres de Kubernetes para escalabilidad masiva de agentes concurrentes.
