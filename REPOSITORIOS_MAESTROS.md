# 🛸 Inventario Maestro de Fuentes, Herramientas & Skills — Ecosistema Antigravity

Este documento constituye el **Catálogo Maestro de Recursos, Repositorios de Código Abierto y Modelos de Frontera** integrados en la célula de agentes de **Antigravity**. Cada recurso está documentado con su descripción técnica, casos de uso prácticos, impacto en el ecosistema y modelo de costos (Gratis, De Pago o Híbrido).

---

## 📑 Índice General
1. [Agentes Autónomos & Frameworks de Orquestación](#1-agentes-autónomos--frameworks-de-orquestación)
2. [GTM, Outbound & Automatización Comercial](#2-gtm-outbound--automatización-comercial)
3. [Memoria Persistente & Knowledge Graphs](#3-memoria-persistente--knowledge-graphs)
4. [Scraping Sigiloso, OSINT & Detección de Tech Stack](#4-scraping-sigiloso-osint--detección-de-tech-stack)
5. [Modelos LLM de Frontera & Enrutadores de Costo Cero](#5-modelos-llm-de-frontera--enrutadores-de-costo-cero)
6. [Developer Tools, UI Loaders & Productividad](#6-developer-tools-ui-loaders--productividad)

---

## 1. Agentes Autónomos & Frameworks de Orquestación

### 🤖 1.1 OpenManus
* **Repositorio:** [FoundationAgents/OpenManus](https://github.com/FoundationAgents/OpenManus)
* **Descripción:** Framework de agentes autónomos multi-herramienta inspirado en Manus AI. Ejecuta tareas en bucle cerrado (Loop-agentic), interactuando dinámicamente con navegadores, ejecutores de código y herramientas sin depender de APIs cerradas.
* **Casos de Uso:** Prospección B2B autónoma, investigación multi-paso de empresas, auditorías de sitios web sin intervención humana.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Infraestructura Agéntica)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source (MIT)**. *(Requiere llaves de API LLM o modelos locales vía Ollama)*.
* **Skill Derivada:** `agent-installer`, `lightpanda-scraping-specialist`

---

### 🐝 1.2 Data Agent Swarms (Powerdrill.ai)
* **Recurso:** [Powerdrill.ai Blog: Data Agent Swarms](https://powerdrill.ai/es/blog/data-agent-swarms-a-new-paradigm-in-agentic-ai)
* **Descripción:** Paradigma arquitectónico donde las tareas complejas de datos no son ejecutadas por un solo agente monolítico, sino por un **enjambre colaborativo de agentes especializados** operando en paralelo con memoria compartida y grafos de ejecución (DAG).
* **Casos de Uso:** Análisis masivo de datos crediticios, ingeniería de datos automatizada, generación de Vibe Intelligence (VI) a partir de grandes volúmenes no estructurados.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Arquitectura de Escala)
* **Modelo de Costo:** **🟡 Híbrido** (El concepto y patrones son 100% aplicables gratis con frameworks open-source; la plataforma Powerdrill.ai tiene planes freemium/enterprise).
* **Skill Derivada:** `data-agent-swarm-orchestrator`

---

### 🤝 1.3 CrewAI
* **Repositorio:** [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
* **Descripción:** Framework líder para orquestar tripulaciones de agentes de IA autónomos basados en roles, delegación de tareas y colaboración estructurada.
* **Casos de Uso:** Creación de agencias virtuales (ej. Investigador + Redactor + Revisor de Compliance) para automatizar procesos comerciales completos.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Estándar de la Industria)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source (MIT)**.
* **Skill Derivada:** `crewai-team-orchestrator`

---

### 🙋‍♂️ 1.4 RAISE (Humansys)
* **Repositorio:** [humansys/raise](https://github.com/humansys/raise)
* **Descripción:** Framework de orquestación de agentes enfocado en la retroalimentación humana continua y alineación (*Human-in-the-Loop*).
* **Casos de Uso:** Procesos donde una decisión automática (como aprobación de crédito o envío de ofertas comerciales) requiere un paso de validación/visto bueno por un ejecutivo humano antes de ejecutarse.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Control de Riesgo)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `hitl-agent-orchestrator`

---

### 🔄 1.5 Hermes Agent (NousResearch)
* **Repositorio:** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
* **Descripción:** Agente autónomo con capacidad de auto-mejora continua. Aprende de las interacciones previas, genera y refina sus propias habilidades (*skills*) y mantiene su propia memoria a lo largo del tiempo.
* **Casos de Uso:** Agente de desarrollo persistente que evoluciona con las reglas de negocio de la empresa y mejora sus propios scripts.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Auto-Evolución)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source (MIT)**.
* **Skill Derivada:** `hermes-self-improving-agent`, `unforget-memory`

---

### 🖥️ 1.6 OpenWorker (Andrew Ng & Rohit Prasad)
* **Repositorio:** [andrewyng/openworker](https://github.com/andrewyng/openworker)
* **Descripción:** Aplicación de escritorio Local-First ("AI Coworker") construida en Tauri 2 + React + Python FastAPI. Ejecuta tareas complejas entregando trabajo terminado de forma segura.
* **Casos de Uso:** Asistente local que ejecuta scripts, prepara reportes y procesa documentos sin enviar información a servidores de terceros de manera innecesaria.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Privacidad & Ejecución Local)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source (BYOK / Ollama)**.
* **Skill Derivada:** `fullstack-developer`, `fastapi-developer`, `it-ops-orchestrator`

---

### 🏢 1.7 Company OS Starter Kit
* **Repositorio:** [Workflowsio/company-os-starter-kit](https://github.com/Workflowsio/company-os-starter-kit)
* **Descripción:** Starter kit para construir un Sistema Operativo Empresarial (Company OS) automatizado con agentes que gestionan flujos operativos y de RevOps.
* **Casos de Uso:** Estandarización de operaciones de venta, onboarding de clientes y tareas administrativas.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Operación B2B)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `company-os-architect`

---

### 📐 1.8 BMAD Method
* **Recurso:** [BMAD Method Docs](https://docs.bmad-method.org/)
* **Descripción:** Metodología sistemática para el diseño, especificación y desarrollo de agentes de IA y arquitecturas de prompt engineering.
* **Casos de Uso:** Estructuración formal de prompts, delimitación de responsabilidades de agentes y evitación de parches superficiales.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Metodología)
* **Modelo de Costo:** **🟢 100% Gratis / Documentación Abierta**.
* **Skill Derivada:** `bmad-architecture-specialist`

---

### 🎯 1.9 DeepSeek Agent Master
* **Repositorio:** [deepseek-ai/awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent)
* **Descripción:** Repositorio curado por DeepSeek AI con patrones, arquitecturas y proyectos construidos sobre modelos DeepSeek-V3 y DeepSeek-R1.
* **Casos de Uso:** Optimización de agentes utilizando modelos razonadores económicos de alto desempeño.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Referencia Técnica)
* **Modelo de Costo:** **🟢 100% Gratis / Open Access**.
* **Skill Derivada:** `deepseek-agent-master`

---

### 🏢 1.10 Agency Agents & Skills
* **Repositorios:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) & [mattpocock/skills](https://github.com/mattpocock/skills)
* **Descripción:** Colecciones de roles agénticos para agencias de desarrollo/marketing y biblioteca de habilidades modulares rápidas.
* **Casos de Uso:** Despliegue rápido de equipos virtuales multidisciplinarios.
* **Impacto:** ⭐⭐⭐ (Medio-Alto - Plantillas Rápidas)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `agency-skills-toolkit`

---

## 2. GTM, Outbound & Automatización Comercial

### ✉️ 2.1 Cold Outbound Email Agents
* **Repositorios:** [rohitchangediya/cold-emailer-public](https://github.com/rohitchangediya/cold-emailer-public) & [Dumebii/free_outbound_email_agent](https://github.com/Dumebii/free_outbound_email_agent)
* **Descripción:** Motores de prospección outbound que automatizan la investigación del prospecto, la redacción de secuencias frías personalizadas (MEDDIC/SPIN) y la entrega sin costo.
* **Casos de Uso:** Campañas de prospección quirúrgica en SOFOMes, Arrendadoras y Fintechs.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Speed to Sell)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `cold-outbound-agent`

---

### 🎓 2.2 18 GTM Agent Skills & Sales Role-Play
* **Recursos:** [18 GTM Agent Skills (Notion)](https://clammy-mangosteen-672.notion.site/18-GTM-Agent-Skills-Turn-Any-AI-Agent-Into-a-GTM-Engineer-35eafe125a16818aa921d9e64a6f15ad) | [Dialfyne AI Role-Play](https://dialfyne.com/services/ai-role-play) | [Attention.com](https://attention.com/product/ask-attention-anything)
* **Descripción:** Guías avanzadas para transformar cualquier agente de IA en un **GTM Engineer** (18 competencias de venta B2B), plataformas de inteligencia en llamadas comerciales y simuladores de roleplay para entrenar ejecutivos de venta (AEs).
* **Casos de Uso:** Preparación del Caso de Negocio para reuniones con tomadores de decisión, entrenamiento de manejo de objeciones y battlecards dinámicas contra competidores (ej. DynamiCore).
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - RevOps & Cierre)
* **Modelo de Costo:** **🟡 Híbrido** (Las guías de Notion y metodologías son 100% gratis; plataformas como Attention y Dialfyne son SaaS de pago).
* **Skill Derivada:** `gtm-engineer-skills`, `sales-roleplay-coach`

---

### 🗺️ 2.3 The AI Agent OS Fully Mapped
* **Recurso:** [The AI Agent OS Fully Mapped (Notion)](https://clammy-mangosteen-672.notion.site/The-AI-Agent-OS-Fully-Mapped-360afe125a1681a9aca5ec2ab046137f)
* **Descripción:** Mapa conceptual y técnico completo del Sistema Operativo de Agentes de IA, abarcando desde la capa de inferencia hasta la interfaz de usuario.
* **Casos de Uso:** Diseño arquitectónico de soluciones empresariales agénticas.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Framework)
* **Modelo de Costo:** **🟢 100% Gratis**.
* **Skill Derivada:** `agent-os-architecture`

---

## 3. Memoria Persistente & Knowledge Graphs

### 🧠 3.1 Unforget Memory
* **Repositorio:** [tecnocriollo/unforget](https://github.com/tecnocriollo/unforget)
* **Descripción:** Sistema de memoria continua y fotográfica para agentes LLM que previene la amnesia de sesión y permite recuperar contexto pasado sin inflar los tokens de entrada.
* **Casos de Uso:** Mantener el hilo de conversaciones y proyectos a lo largo de semanas de desarrollo.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Persistencia)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `unforget-memory`

---

### 🏰 3.2 Memory Palace
* **Repositorio:** [milla-jovovich/mempalace](https://github.com/milla-jovovich/mempalace)
* **Descripción:** Estructura de "palacio de la memoria" jerárquico para agentes de contexto ultra-largo, organizando conceptos en habitaciones y estantes virtuales.
* **Casos de Uso:** Organización de bases de datos de conocimiento complejas y documentación técnica de gran tamaño.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Estructura de Datos)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `memory-palace-architect`

---

### 📓 3.3 Obsidian Skills & Copilot
* **Repositorios:** [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | [logancyang/obsidian-copilot](https://github.com/logancyang/obsidian-copilot) | [your-papa/obsidian-Smart2Brain](https://github.com/your-papa/obsidian-Smart2Brain)
* **Descripción:** Integración nativa de agentes e Inteligencia Artificial dentro de bóvedas de notas en Markdown (Obsidian), permitiendo razonar sobre notas locales.
* **Casos de Uso:** Gestión del conocimiento personal (PKM), documentación de proyectos y sincronización de notas de reuniones.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Productividad)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `obsidian-vault-agent`, `obsidian-smart-brain`

---

### 🕸️ 3.4 Graphify & MiroFish
* **Repositorios:** [safishamsi/graphify](https://github.com/safishamsi/graphify) & [666ghj/MiroFish](https://github.com/666ghj/MiroFish)
* **Descripción:** Herramientas para convertir código, texto no estructurado y relaciones B2B en Grafos de Conocimiento interactivos (Knowledge Graphs).
* **Casos de Uso:** Mapeo de relaciones entre grupos financieros, SOFOMes, fundadores y filiales.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Inteligencia de Datos)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `knowledge-graphify`, `visual-graph-scout`

---

## 4. Scraping Sigiloso, OSINT & Detección de Tech Stack

### 🕵️‍♂️ 4.1 Stealth Browser MCP
* **Repositorio:** [vibheksoni/stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)
* **Descripción:** Servidor MCP (Model Context Protocol) que expone un navegador Puppeteer/Playwright con técnicas anti-detección (evasión de Cloudflare, Akamai y recaptchas).
* **Casos de Uso:** Scraping agéntico en portales regulados o sitios web protegidos contra bots.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Extracción de Datos)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `stealth-browser-mcp`

---

### 🔍 4.2 OSINTNova Platform
* **Recurso:** [OSINTNova Platform](https://osintnova.com/#osintnova-platform)
* **Descripción:** Plataforma de Inteligencia de Fuentes Abiertas (OSINT) diseñada para investigación profunda de huella digital, dominios, ejecutivos y estructuras corporativas.
* **Casos de Uso:** Due diligence pre-credito, validación de ejecutivos clave y verificación de legitimidad comercial.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Risk & Compliance)
* **Modelo de Costo:** **🟡 Híbrido** (Herramientas abiertas OSINT son gratis; la plataforma unificada OSINTNova ofrece tiers freemium y pro).
* **Skill Derivada:** `osint-investigator`

---

### ⚡ 4.3 Tech Stack Analyzer & Wappalyzer API
* **Repositorios:** [thankyo/wappalyzer-api](https://github.com/thankyo/wappalyzer-api) & [CarlosVallejoRuiz/slurp](https://github.com/CarlosVallejoRuiz/slurp)
* **Descripción:** APIs y scripts de extracción rápida para identificar las tecnologías utilizadas por un sitio web (procesador de pagos, core bancario, CRM, widgets) y limpiar el HTML a texto plano.
* **Casos de Uso:** Detectar qué SOFOMes usan competidores (ej. DynamiCore) o qué pasarelas de pago tienen integradas.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Inteligencia Competitiva)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source (Self-hosted)**.
* **Skill Derivada:** `tech-stack-analyzer`, `slurp-data-extractor`

---

## 5. Modelos LLM de Frontera & Enrutadores de Costo Cero

### 🌕 5.1 Kimi-K3 (Moonshot AI)
* **Modelo:** [moonshotai/Kimi-K3 en Hugging Face](https://huggingface.co/moonshotai/Kimi-K3)
* **Descripción:** Modelo abierto MoE (Mixture of Experts) de **2.8 Trillones de Parámetros** con ventana de contexto nativa de **1 Millón de tokens** y multimodalidad.
* **Casos de Uso:** Razonamiento sobre expedientes crediticios y regulaciones masivas en una sola llamada en la nube.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Modelo de Frontera)
* **Modelo de Costo:** **🟡 Híbrido** (Pesos 100% gratis bajo licencia Kimi K3; requiere hardware masivo para hosting local o pago por token vía API remota).
* **Skill Derivada:** `llm-architect`

---

### 🔀 5.2 Free AI API Routers & Resources
* **Repositorios:** [topics/free-ai-api](https://github.com/topics/free-ai-api) | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | [andres20980/claude-free](https://github.com/andres20980/claude-free)
* **Descripción:** Directorios y enrutadores para aprovechar las capas gratuitas (free tiers) de proveedores de IA como Groq, Google AI Studio (Gemini 1.5 Pro/Flash), Together AI y Cloudflare Workers AI.
* **Casos de Uso:** Ejecución de agentes continuos a costo cero ($0 USD) utilizando proveedores con cuotas gratuitas generosas.
* **Impacto:** ⭐⭐⭐⭐⭐ (Muy Alto - Eficiencia Financiera)
* **Modelo de Costo:** **🟢 100% Gratis / Free Tiers**.
* **Skill Derivada:** `zero-cost-llm-router`, `claude-free-router`

---

## 6. Developer Tools, UI Loaders & Productividad

### 🎨 6.1 GitHub Topics: Loader
* **Recurso:** [GitHub Topics: Loader](https://github.com/topics/loader)
* **Descripción:** Colección de librerías y componentes UI para implementar animaciones de carga (*skeleton screens / shimmer loaders*) en aplicaciones web.
* **Casos de Uso:** Dar apariencia instantánea y premium a las aplicaciones web de Antigravity (estilo Linear/Vercel) mientras los agentes procesan datos en segundo plano.
* **Impacto:** ⭐⭐⭐⭐ (Alto - UX Premium)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `ui-designer`, `agentic-cms-architect`

---

### 🎙️ 6.2 HeyHank
* **Repositorio:** [heyhank-app/heyhank](https://github.com/heyhank-app/heyhank)
* **Descripción:** Asistente conversacional de voz en tiempo real con integración de baja latencia.
* **Casos de Uso:** Prototipado de interfaces conversacionales de voz para módulos de atención o cobranza en fintechs.
* **Impacto:** ⭐⭐⭐ (Medio - Futuras Funcionalidades)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `websocket-engineer`, `nlp-engineer`

---

### 📋 6.3 Paperclip & Superpowers CLI
* **Repositorios:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip) & [obra/superpowers](https://github.com/obra/superpowers)
* **Descripción:** Herramientas de captura rápida de contexto en pantalla y utilidades CLI de alta velocidad para desarrolladores.
* **Casos de Uso:** Ingestión rápida de fragmentos de código y automatización de comandos en la consola.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Productividad DX)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `context-clip-manager`, `cli-superpowers`

---

### 🧪 6.4 Argilla & AI Toolkit
* **Recursos:** [Argilla Docs](https://docs.argilla.io/) & [ostris/ai-toolkit](https://github.com/ostris/ai-toolkit)
* **Descripción:** Plataforma de curaduría de datos para entrenamiento/evaluación de LLMs (Argilla) y toolkit para entrenamiento de modelos visuales/LoRAs.
* **Casos de Uso:** Fine-tuning de modelos especializados en jerga bancaria mexicana y curaduría de datasets.
* **Impacto:** ⭐⭐⭐⭐ (Alto - ML Ops)
* **Modelo de Costo:** **🟢 100% Gratis / Open-Source**.
* **Skill Derivada:** `argilla-data-curator`, `ai-toolkit-trainer`

---

### ⚡ 6.5 MCP Server Serper & GitNexus
* **Repositorios:** [marcopesani/mcp-server-serper](https://github.com/marcopesani/mcp-server-serper) & [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)
* **Descripción:** Servidores MCP para integración inmediata de búsquedas en Google vía Serper API y navegador de grafos de repositorios Git.
* **Casos de Uso:** Búsquedas web ultra-rápidas para agentes de investigación y análisis de repositorios extensos.
* **Impacto:** ⭐⭐⭐⭐ (Alto - Herramientas MCP)
* **Modelo de Costo:** **🟡 Híbrido** (Servidor MCP open-source gratis; la API de Serper tiene cuota gratuita inicial y luego pago por consulta).
* **Skill Derivada:** `serper-search-mcp`, `git-nexus-orchestrator`

---

*Documento mantenido y actualizado por la Célula de Agentes de Antigravity.*
