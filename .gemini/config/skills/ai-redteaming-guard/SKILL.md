---
name: ai-redteaming-guard
description: Evaluación de riesgos de seguridad en infraestructura de IA, agentes, servidores MCP, envenenamiento de herramientas y pruebas de jailbreak inspirado en Tencent/AI-Infra-Guard.
---

# Skill: AI Red Teaming & Infra Guard

## Propósito
Realizar pruebas de seguridad adversarias (Red Teaming) en agentes de IA, evaluar vulnerabilidades en servidores MCP (Model Context Protocol), detectar envenenamiento de herramientas (tool poisoning) y audits de infraestructura LLM (CVEs en Ollama, ComfyUI, etc.).

## Pilares de Evaluación
1. **MCP & Tool Security Scan:**
   - Detectar inyección de instrucciones maliciosas en parámetros de herramientas MCP y payloads no sanitizados.
2. **LLM Jailbreak & Adversarial Audit:**
   - Evaluación contra prompts engañosos o intentos de evasión de guardrails de seguridad.
3. **Agentes & Workflows (ClawScan / AgentScan):**
   - Inspección de bucles agénticos para prevenir ejecuciones no autorizadas de comandos del sistema o fuga de variables de entorno.
