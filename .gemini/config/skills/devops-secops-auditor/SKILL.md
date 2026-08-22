---
name: devops-secops-auditor
description: Auditoría de seguridad, DevSecOps, hardening de contenedores, revisión de Terraform/Kubernetes y cumplimiento normativo (SOC2, ISO27001, HIPAA, PCI-DSS) basado en BagelHole/devops-security-agent-skills.
---

# Skill: DevOps & SecOps Auditor

## Propósito
Esta skill provee pautas, checklists y playbooks de auditoría para asegurar la infraestructura en la nube, hardening de Docker/Kubernetes, análisis de Terraform/IaC y cumplimiento normativo automatizado en los proyectos del workspace.

## Capacidades Principales
1. **Auditoría de Infraestructura como Código (IaC):**
   - Validación de archivos `.tf` (Terraform) y manifiestos de Kubernetes buscando secretos expuestos, permisos excesivos (RBAC) y configuraciones inseguras.
2. **Hardening de Contenedores:**
   - Verificación de Dockerfiles: evitar ejecución como `root`, multi-stage builds, uso de imágenes base distroless/alpine y escaneo de vulnerabilidades.
3. **Cumplimiento Normativo (Compliance Checks):**
   - Verificaciones automatizadas para estándares SOC2 Type II, ISO 27001, HIPAA, GDPR y PCI-DSS.
4. **LLMOps & Secret Management:**
   - Auditoría de gestión de llaves API (Groq, Deepgram, OpenAI, Gemini) evitando harcodeo en código fuente o repositorios Git.

## Comandos y Flujo de Auditoría
- **Checklist IaC / Docker:**
  - Ejecutar escaneo estático de manifiestos y variables de entorno.
  - Verificar que todo secreto consuma `process.env` o `.env.local` excluido en `.gitignore`.
